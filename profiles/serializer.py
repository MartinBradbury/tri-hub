from rest_framework import serializers
from .models import Profile
from followers.models import Follower
import datetime

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    post_count = serializers.ReadOnlyField()
    follower_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    date_of_birth = serializers.DateField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    def validate_date_of_birth(self, obj):
        if obj > datetime.date.today():
            print("Cannot be in the future")
            raise serializers.ValidationError("Date cannot be in the future.")
        # Calculate age
        today = datetime.date.today()
        age = today.year - obj.year - ((today.month, today.day) < (obj.month, obj.day))
        if age < 18:
            self.context['can_create_training_plan'] = False
            print("Under 18. Cannot create a training plan.")
        return obj


    class Meta:
        model = Profile
        fields = ['id', 'owner', 'created_at', 'updated_at',
                 'first_name', 'last_name',
                  'email', 'gender', 'fitness_level', 
                  'image', 'content', 'is_owner', 'following_id',
                  'follower_count', 'following_count', 'post_count',
                  'date_of_birth',
                  ]
            