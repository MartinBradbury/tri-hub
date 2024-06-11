from rest_framework import serializers
from .models import Goal
from django.utils import timezone
from datetime import timedelta
from django.contrib.humanize.templatetags.humanize import naturaltime

class GoalSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    event_date = serializers.DateField(format='%d-%m-%Y') 
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)


    def validate_event_date(self, obj):
        today = timezone.now().date()
        three_weeks_from_today = today + timedelta(weeks=3)
        
        if obj < today or obj <= three_weeks_from_today:
            raise serializers.ValidationError("The event date must be a minimum of 3 weeks from today.")
        return obj

    class Meta:
        model = Goal
        fields = [
                'id', 'owner', 'event_date', 'content', 'hours_per_week',
                'completed', 'created_at', 'updated_at', 'is_owner',           
         ]

