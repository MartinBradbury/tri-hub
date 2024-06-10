from rest_framework import serializers
from .models import UserPerformance, Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'distance',]

