from rest_framework import serializers
from .models import TrainingPlan
from django.contrib.humanize.templatetags.humanize import naturaltime

class TrainingPlanSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = TrainingPlan
        fields = ['id', 'owner', 'title', 'created_at', 
                'updated_at','is_owner', 'plan_level', 'hours_available',
                'weeks_available', 'content', 'notes', 'complete',
                ]