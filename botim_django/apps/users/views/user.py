from django.shortcuts import render
from ..models import User
from ..serializers import UserSerializer,UserCreateSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView


class UserRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()