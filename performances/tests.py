from django.contrib.auth.models import User
from django.utils import timezone
from .models import Event, UserPerformance
from rest_framework import status
from rest_framework.test import APITestCase


class EventViewTests(APITestCase):
    def setUp(self):
        self.user_jacob = User.objects.create_user(
            username='jacob', password='pw'
        )
        self.user_john = User.objects.create_user(
            username='john', password='pw2'
        )

    def test_can_list_events_unauthenticated(self):
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_list_events_authenticated(self):
        self.client.login(username='jacob', password='pw')
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_specific_user_can_create_Events(self):
        self.client.login(username='jacob', password='pw')
        Event.objects.create(
            title='Test', description='test description', distance=50
        )
        events = Event.objects.all()
        self.assertIn(
            'Test',
            [event.title for event in events],
            "An event with title 'Test' should exist."
        )

    def test_non_specific_user_cannot_create_Events(self):
        response = self.client.post('/events/', {
            'title': 'UnAuth Test',
            'description': 'test description',
            'distance': 50
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class UserPerformanceViewTests(APITestCase):
    def setUp(self):
        self.user_jacob = User.objects.create_user(
            username='jacob', password='pw'
        )
        self.user_john = User.objects.create_user(
            username='john', password='pw2'
        )

        Event.objects.create(
            title='Test',
            description='test description',
            distance=50
        )

    def test_can_list_userperformances_unauthenticated(self):
        response = self.client.get('/performances/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_list_userperformances_authenticated(self):
        self.client.login(username='jacob', password='pw')
        response = self.client.get('/performances/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_create_performance(self):
        self.client.login(username='jacob', password='pw')
        UserPerformance.objects.create(
            owner=self.user_jacob,
            event_id=1,
            time='10:10:10',
            complete_date=timezone.now(),
            content='New Performance'
        )
        up = UserPerformance.objects.all()
        self.assertIn(
            'New Performance',
            [up.content for up in up],
            "An event with content 'New Performance' should exist."
        )

    def test_non_auth_cannot_create_peformance(self):
        response = self.client.post('/performances/', {
            'event_id': 1,
            'time': '10:10:10',
            'completed_date': timezone.now(),
            'content': 'Performance',
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_cannot_create_performance_in_future(self):
        self.client.login(username='jacob', password='pw')
        response = self.client.post('/performances/', {
            'owner': self.user_jacob.id,
            'event_id': 1,
            'time': '10:10:10',
            'complete_date': (timezone.now() + timezone.timedelta(days=365)),
            'content': 'New Performance'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
