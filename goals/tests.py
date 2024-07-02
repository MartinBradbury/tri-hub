from django.contrib.auth.models import User
from django.utils import timezone
from .models import Goal
from rest_framework import status
from rest_framework.test import APITestCase


class GoalViewTests(APITestCase):
    def setUp(self):
        self.user_jacob = User.objects.create_user(
            username='jacob', password='pw'
        )
        self.user_john = User.objects.create_user(
            username='john', password='pw2'
        )

        Goal.objects.create(
            owner=self.user_jacob,
            event_date=timezone.now() + timezone.timedelta(days=365),
            hours_per_week=1,
            content='Jacob\'s Test Goal'
        )

        Goal.objects.create(
            owner=self.user_john,
            event_date=timezone.now() + timezone.timedelta(days=365),
            hours_per_week=1,
            content='John\'s Test Goal'
        )

    def test_can_list_goals_unauthenticated(self):
        response = self.client.get('/goals/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_list_goals_authenticated(self):
        self.client.login(username='jacob', password='pw')
        response = self.client.get('/goals/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_create_goals_unauthenticated(self):
        response = self.client.post('/goals/', {
            'owner': self.user_john,
            'event_date': timezone.now() + timezone.timedelta(days=365),
            'hours_per_week': 1,
            'content': 'unauthenticated goal'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_create_goals_when_authenticated(self):
        self.client.login(username='jacob', password='pw')
        Goal.objects.create(
            owner=self.user_jacob,
            event_date=timezone.now() + timezone.timedelta(days=365),
            hours_per_week=1,
            content='New'
        )
        goals = Goal.objects.all()
        self.assertIn(
            'New',
            [goal.content for goal in goals],
            "A goal with content 'New' should exist."
        )
