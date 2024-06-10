from rest_framework import serializers
from .models import Goal

class GoalSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    event_date = serializers.DateField(format='%d-%m-%Y') 
    

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner


    class Meta:
        model = Goal
        fields = [
                'id', 'owner', 'event_date', 'content', 'hours_per_week',
                'completed', 'created_at', 'updated_at', 'is_owner',           
         ]

