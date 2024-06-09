from django.db import models
from django.contrib.auth.models import User
from Profiles.models import Profile


"""
Goals Model that the user will populate to be assigned a training plan. 
"""
class Goal(models.Model):

    """
    Choices for the hours available to train per week.
    """
    HOURS_CHOICES = [
    (1, '3 Hours'),
    (2, '6 Hours'),
    (3, '9 Hours'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event_date = models.DateField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=500, blank=True)
    hours_per_week = models.IntegerField(
        choices=HOURS_CHOICES,
        default=1,
    )
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner}s Goals'

