from .models import Profile, Portfolio, Like, Comment
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'nickName', 'profileUser', 'created_on', 'img')
        extra_kwargs = {'profileUser': {'read_only': True}}


class PortfolioSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Portfolio
        fields = ('id', 'title', 'url', 'author', 'created_on', 'img')
        extra_kwargs = {'author': {'read_only': True}}


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'likeUser', 'likePortfolio')
        extra_kwargs = {'likeUser': {'read_only': True}}


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'commentUser', 'commentPortfolio')
        extra_kwargs = {'commentUser': {'read_only': True}}
