from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from ..models import DayKind
from ..serializers import GetDayKindSerializer


class DayKindListAPIView(ListAPIView):
    queryset = DayKind.objects.all()
    serializer_class = GetDayKindSerializer


class DayKindRetrieveAPIView(RetrieveAPIView):
    queryset = DayKind.objects.all()
    serializer_class = GetDayKindSerializer
    

