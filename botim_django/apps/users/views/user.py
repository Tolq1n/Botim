from django.shortcuts import render
from ..models import User
from ..serializers import UserSerializer
from rest_framework.generics import RetrieveAPIView

class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()