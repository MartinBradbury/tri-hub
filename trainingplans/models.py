from django.db import models
from django.contrib.auth.models import User
from goals.models import Goal


class TrainingPlan(models.Model):

    """
    Choices for the difficulty of the training plan.
    """
    PLAN_DIFFICULTY = [
        (1, 'Easy'),
        (2, 'Medium'),
        (3, 'Hard'),
        ]

    """
    Choices for the hours available to train per week.
    """
    HOURS_CHOICES = [
        (1, '3 Hours'),
        (2, '6 Hours'),
        (3, '9 Hours'),
    ]

    """
    Choices for the weeks available to train per week.
    """
    WEEKS = [
        (1, '3 Weeks'),
        (2, '6 Weeks'),
        (3, '9 Weeks'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    plan_level = models.IntegerField(
        choices=PLAN_DIFFICULTY,
        default=1,
    )
    hours_available = models.IntegerField(
        choices=HOURS_CHOICES,
        default=1,
    )
    weeks_available = models.IntegerField(
        choices=WEEKS,
        default=1,
    )
    content = models.TextField(blank=False)
    notes = models.TextField(blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return (
            f"{self.title} - "
            "Level: {self.plan_level} - "
            "Hours/Week: {self.hours_available} - "
            "Weeks: {self.weeks_available}"
        )

    class Meta:
        ordering = ["-plan_level", "-hours_available", "-weeks_available"]
