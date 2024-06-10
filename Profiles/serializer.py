from rest_framework import serializers
from .models import Profile
from Followers.models import Follower

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    post_count = serializers.ReadOnlyField()
    follower_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

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


    class Meta:
        model = Profile
        fields = ['id', 'owner', 'created_at', 'updated_at',
                 'first_name', 'last_name',
                  'email', 'gender', 'fitness_level', 
                  'image', 'content', 'is_owner', 'following_id',
                  'follower_count', 'following_count', 'post_count',
                  ]
            