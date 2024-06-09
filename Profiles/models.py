from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

MALE = 'M'
FEMALE = 'F'
OTHER = 'O'
NOT_IDENTIFIED = 'N'

HIGH = 'H'
MEDIUM = 'M'
LOW = 'L'
UNKNOWN = 'U'


"""
Profile Model that is created when a new user is created. 
"""
class Profile(models.Model):

    """
    Gender_Choices
    """
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
        (NOT_IDENTIFIED, 'Not Identified'),
    ]


    """
    Fitness_level Choices
    """
    FITNESS_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
        (UNKNOWN, 'Unknown')
    ]


    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=NOT_IDENTIFIED,
    )
    fitness_level = models.CharField(
        max_length=1,
        choices=FITNESS_CHOICES,
        default=UNKNOWN,
    )
    image = models.ImageField(
        upload_to = 'images/', default='../default_profile_qtk8ec'
    )
    content = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


"""
django signals to profile is created every time a user is created.
"""
post_save.connect(create_profile, sender=User)

