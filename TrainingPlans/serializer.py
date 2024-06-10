from rest_framework import serializers
from .models import TrainingPlan

class TrainingPlanSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = TrainingPlan
        fields = ['id', 'owner', 'title', 'created_at', 
                'updated_at','is_owner', 'plan_level', 'hours_available',
                'weeks_available', 'content', 'notes', 'complete',
                ]