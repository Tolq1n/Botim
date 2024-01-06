from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from ..models import WeekDay
from ..serializers import GetWeekDaySerializer


class WeekDayListAPIView(ListAPIView):
    queryset = WeekDay.objects.all()
    serializer_class = GetWeekDaySerializer

class WeekDayRetrieveAPIView(RetrieveAPIView):
    queryset = WeekDay.objects.all()
    serializer_class = GetWeekDaySerializer


