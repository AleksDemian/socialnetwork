from rest_framework import serializers
from django.contrib.auth.models import User

from feed.models import Post, Comments
from users.models import Profile


class UserSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    friends = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'image', 'slug', 'friends']


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.username')

    def create(self, validated_data):
        return Comments.objects.create(**validated_data)

    class Meta:
        model = Comments
        fields = ['id', 'post', 'username', 'comment', 'comment_date']


class PostSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user_name.username')
    details = serializers.SlugRelatedField(many=True, read_only=True, slug_field='comment')

    class Meta:
        model = Post
        fields = ['id', 'user_name', 'description', 'pic', 'date_posted', 'tags', 'details']
