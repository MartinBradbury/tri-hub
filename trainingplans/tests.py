from django.contrib.auth.models import User
from django.utils import timezone
from .models import TrainingPlan
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

    def test_can_list_trainingplans_unauthenticated(self):
        response = self.client.get('/trainingplans/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_list_trainingplans_authenticated(self):
        self.client.login(username='jacob', password='pw')
        response = self.client.get('/trainingplans/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)



