from rest_framework import serializers
from django.utils import timezone
from .models import UserPerformance, Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'distance', ]

        def validate_id(self, value):
            if not isinstance(value, int):
                raise serializers.ValidationError("ID must be an integer")
            return value


class PerformanceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    title = serializers.ReadOnlyField(source='event.title')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def validate_complete_date(self, value):
        today = timezone.now().date()
        if value > today:
            raise serializers.ValidationError(
                "The complete_date must be today or a previous date."
            )
        return value

    class Meta:
        model = UserPerformance
        fields = [
                'id', 'owner', 'event', 'time',
                'complete_date', 'is_owner', 'title', 'content',
                ]
