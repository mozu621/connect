from . import serializers
from rest_framework import generics
from rest_framework.permissions import AllowAny


class CreateUserView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)
