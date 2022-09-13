from .models import Profile, Portfolio, Like, Comment, Tag
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'nickName', 'introduction', 'career', 'profileUser', 'created_on', 'img', 'githuburl', 'twitterurl', )
        extra_kwargs = {'profileUser': {'read_only': True}}


class PortfolioSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)


    class Meta:
        model = Portfolio
        fields = ('id', 'title', 'url',  'content', 'author', 'created_on', 'img')
        extra_kwargs = {'author': {'read_only': True}}


class PopularSerializer(serializers.ModelSerializer):
    likes = serializers.IntegerField()
    created_on = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Portfolio
        fields = ('id', 'title', 'url',  'content', 'author', 'created_on', 'img', 'likes')
        extra_kwargs = {'author': {'read_only': True}}        


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'likeUser', 'likePortfolio',)
        extra_kwargs = {'likeUser': {'read_only': True}}
        


class CommentSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'commentUser', 'commentPortfolio', 'created_on')
        extra_kwargs = {'commentUser': {'read_only': True}}

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        depth = 1
        fields = ('id', 'tagname','tagPortfolio')

class TagPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag

        fields = ('id', 'tagname','tagPortfolio')

