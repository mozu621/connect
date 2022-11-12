
from rest_framework import viewsets
from app.serializers import  ProfileSerializer, PortfolioSerializer, LikeSerializer, PopularSerializer, CommentSerializer, TagSerializer, TagPostSerializer
from rest_framework import generics
from app.models import Profile, Portfolio, Like, Comment, Tag
from rest_framework.permissions import AllowAny
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (AllowAny,)


    def perform_create(self, serializer):
        serializer.save(profileUser=self.request.user)


class MyProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return self.queryset.filter(profileUser=self.request.user)



class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = (AllowAny,)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def perform_create(self, serializer):

        serializer.save(author=self.request.user)





class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(likeUser=self.request.user)



class PopularViewSet(generics.ListAPIView):
    queryset = Portfolio.objects.annotate(likes=Count('likePortfolio')).order_by('-likes')
    serializer_class = PopularSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(likeUser=self.request.user) 

class FiliterLikeList(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['likePortfolio',]
    permission_classes = (AllowAny,)

class FiliterLikePortfolio(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['likeUser',]
    permission_classes = (AllowAny,)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(commentUser=self.request.user)

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)

class TagPostViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagPostSerializer
    permission_classes = (AllowAny,)    

class FiliterTagList(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tagname',]
    permission_classes = (AllowAny,)


