from rest_framework import serializers
from .models import UserPerformance, Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'distance',]

class PerformanceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    title = serializers.ReadOnlyField(source='event.title')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = UserPerformance
        fields = ['id', 'owner', 'event', 'time', 
                'complete_date','is_owner', 'title', 'content',
                ]