from rest_framework import serializers
from .models import Goal
from django.utils import timezone
from datetime import timedelta

class GoalSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    event_date = serializers.DateField(format='%d-%m-%Y') 
    

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

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

