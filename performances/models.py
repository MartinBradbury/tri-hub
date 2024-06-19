from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    distance = models.FloatField(help_text="Distance in kilometers")

    def __str__(self):
        return f"{self.id}: {self.title}"

    class Meta:
        ordering = ['-distance']


    
class UserPerformance(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    time = models.TimeField(help_text="Enter time in HH:MM:SS format", blank=False)
    complete_date = models.DateField(blank=False)
    content = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.owner.username}'s performance in {self.event.title} "

    class Meta:
        ordering = ['-event']