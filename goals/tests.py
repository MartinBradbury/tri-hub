from django.contrib.auth.models import User
from django.utils import timezone
from.models import Goal
from rest_framework import status
from rest_framework.test import APITestCase

class GoalViewTests(APITestCase):
    def setUp(self):
        # Create two users for testing purposes
        self.user_jacob = User.objects.create_user(username='jacob', password='pw')
        self.user_john = User.objects.create_user(username='john', password='pw2')
        # Create a goal for Jacob
        Goal.objects.create(owner=self.user_jacob, event_date=timezone.now() + timezone.timedelta(days=365), hours_per_week=1, content='Jacob\'s Test Goal')
        # Create a goal for John
        Goal.objects.create(owner=self.user_john, event_date=timezone.now() + timezone.timedelta(days=365), hours_per_week=1, content='John\'s Test Goal')

    def test_can_list_goals_unauthenticated(self):
        # Attempt to get goals without logging in
        response = self.client.get('/goals/')
        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_list_goals_authenticated(self):
        # Log in as Jacob
        self.client.login(username='jacob', password='pw')
        response = self.client.get('/goals/')
        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_cannot_create_goals_unauthenticated(self):
        # Attempt to create a goal without logging in
        response = self.client.post('/goals/', {
            'owner': self.user_john,  
            'event_date': (timezone.now() + timezone.timedelta(days=365)),
            'hours_per_week': 1,
            'content': 'unauthenticated goal'
        })
        # Assert that the response status code indicates unauthorized access
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_create_goals_when_authenticated(self):
        # Login as Jacob
        self.client.login(username='jacob', password='pw')
        # Create a goal with the content 'New'
        Goal.objects.create(owner=self.user_jacob, event_date=timezone.now() + timezone.timedelta(days=365), hours_per_week=1, content='New')
        # Retrieve all goals
        goals = Goal.objects.all()
        # Filter goals by content and assert that at least one goal with content 'New' exists
        self.assertIn('New', [goal.content for goal in goals], "A goal with content 'New' should exist.")