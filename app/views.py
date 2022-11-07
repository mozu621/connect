
from rest_framework import viewsets
from connect.app import serializers
from rest_framework import generics
from connect.app.models import Profile, Portfolio, Like, Comment, Tag
from rest_framework.permissions import AllowAny
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = (AllowAny,)


    def perform_create(self, serializer):
        serializer.save(profileUser=self.request.user)


class MyProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return self.queryset.filter(profileUser=self.request.user)



class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = serializers.PortfolioSerializer
    permission_classes = (AllowAny,)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def perform_create(self, serializer):

        serializer.save(author=self.request.user)





class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer

    def perform_create(self, serializer):
        serializer.save(likeUser=self.request.user)


class PopularViewSet(generics.ListAPIView):
    queryset = Portfolio.objects.annotate(likes=Count('likePortfolio')).order_by('-likes')
    serializer_class = serializers.PopularSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(likeUser=self.request.user) 

class FiliterLikeList(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['likePortfolio',]
    permission_classes = (AllowAny,)

class FiliterLikePortfolio(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['likeUser',]
    permission_classes = (AllowAny,)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def perform_create(self, serializer):
        serializer.save(commentUser=self.request.user)

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = (AllowAny,)

class TagPostViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = serializers.TagPostSerializer
    permission_classes = (AllowAny,)    

class FiliterTagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tagname',]
    permission_classes = (AllowAny,)


