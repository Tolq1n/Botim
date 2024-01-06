from django.shortcuts import render
from ..models import Schedule
from ..serializers import GetSchedulesSerializer, PostSchedulesSerializer
from rest_framework.generics import RetrieveDestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ScheduleListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        data = request.data 

        weekday_id = data['weekday_id']
        user_id = data["user_id"]
        print(weekday_id, user_id)


        schedule = Schedule.objects.filter(user_id=user_id, weekday_id=weekday_id)
        serialized = PostSchedulesSerializer(schedule, many=True, context={'request':request})
        return Response(serialized.data, status=status.HTTP_200_OK)


class ScheduleRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = GetSchedulesSerializer


class ScheduleUpdateAPIView(UpdateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = PostSchedulesSerializer

    http_method_names = ['patch']


class ScheduleCreateAPIView(CreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = PostSchedulesSerializer