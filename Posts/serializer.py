from rest_framework import serializers
from .models import Post
from Likes.models import Like

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    Like_id = serializers.SerializerMethodField()
    Likes_count = serializers.ReadOnlyField()
    comment_count = serializers.ReadOnlyField()
    

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_Like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size is too large, 2MB maximum.'
            )
        if value.image.width > 4096:
            raise serializer.ValidationError(
                'Image width is too large, 4096px maximum'
            )
        if value.image.height > 4096:
            raise serializer.ValidationError(
                'Image height is too large, 4096 maximum'
            )
        return value

    class Meta:
        model = Post
        fields = ['id', 'owner', 'created_at', 'updated_at', 'title', 'content',
                  'image', 'is_owner', 'profile_id', 'profile_image', 'Like_id',
                  'Likes_count', 'comment_count',]
            