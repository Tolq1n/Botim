from django.shortcuts import render
from ..models import Schedule
from ..serializers import GetSchedulesSerializer, PostSchedulesSerializer
from rest_framework.generics import RetrieveDestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import get_language_from_path, get_language_from_request

import time 
from datetime import datetime, timedelta
from pprint import pprint

SHORT_DAY_NAMES_EN = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

SHORT_DAY_NAMES_RU = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

SHORT_DAY_NAMES_UZ = ['Du', 'Se', 'Chor', 'Pay', 'Jum', 'Shan', 'Yak']

class WeekAPIView(APIView):
    def get(self, request):
        language = get_language_from_path(request.path)
        today = datetime.now()
        start_of_week = today - timedelta(days=today.weekday())
        days_of_week = [start_of_week + timedelta(days=x) for x in range(7)]
        SHORT_DAY_NAMES = SHORT_DAY_NAMES_UZ if language == 'uz' else SHORT_DAY_NAMES_RU if language == 'ru' else SHORT_DAY_NAMES_EN
        week_data = [{'day': day.strftime('%Y-%m-%d'), 'name': name} for day, name in zip(days_of_week, SHORT_DAY_NAMES)]
        pprint(week_data)


# def test_function():
#     today = datetime.now()
#     start_of_week = today - timedelta(days=today.weekday())
#     print("startof week", start_of_week)
#     end_of_week = start_of_week + timedelta(days=6)
#     days_of_week = [start_of_week + timedelta(days=x) for x in range(7)]
#     print("days of week", days_of_week)
#     day_names = [day.strftime('%A') for day in days_of_week]
#     print("day names", day_names)
#     # Create a dictionary with days and names
#     week_data = [{'day': day.strftime('%Y-%m-%d'), 'name': name} for day, name in zip(days_of_week, day_names)]
#     pprint(week_data)