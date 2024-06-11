from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile


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

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    event_date = models.DateField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=500, blank=True)
    hours_per_week = models.IntegerField(
        choices=HOURS_CHOICES,
        default=1,
    )
    completed = models.BooleanField(default=False)


    """
    Replacing Goal for user and saving to db
    """
    def save(self, *args, **kwargs):
        # Check if the goal already exists for the user
        existing_goal = Goal.objects.filter(owner=self.owner).first()
        if existing_goal:
            # Delete the existing goal before saving the new one
            existing_goal.delete()
        super().save(*args, **kwargs)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner}s Goal'

