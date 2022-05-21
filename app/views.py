from rest_framework import viewsets
from . import serializers
from rest_framework import generics
from .models import Profile, Portfolio, Like, Comment, Tag
from rest_framework.permissions import AllowAny


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = (AllowAny,)


    def perform_create(self, serializer):
        serializer.save(profileUser=self.request.user)


class MyProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

    def get_queryset(self):
        return self.queryset.filter(profileUser=self.request.user)


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = serializers.PortfolioSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):

        serializer.save(author=self.request.user)


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer

    def perform_create(self, serializer):
        serializer.save(likeUser=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def perform_create(self, serializer):
        serializer.save(commentUser=self.request.user)

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = (AllowAny,)




