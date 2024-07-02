from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile


class Goal(models.Model):

    HOURS_CHOICES = [
        (1, '3 Hours'),
        (2, '6 Hours'),
        (3, '9 Hours'),
        ]

    LENGTH_CHOICES = [
        (1, '3 Weeks'),
        (2, '6 Weeks'),
        (3, '9 Weeks'),
        ]

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    event_date = models.DateField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=500, blank=True)
    plan_length = models.IntegerField(
        choices=LENGTH_CHOICES,
        default=1,
    )
    hours_per_week = models.IntegerField(
        choices=HOURS_CHOICES,
        default=1,
    )
    completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        existing_goal = Goal.objects.filter(owner=self.owner).first()
        if existing_goal:
            existing_goal.delete()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner}s Goal'
