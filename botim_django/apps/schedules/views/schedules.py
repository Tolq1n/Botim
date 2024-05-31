from django.shortcuts import render
from ..models import Schedule
from ..serializers import GetSchedulesSerializer, PostSchedulesSerializer
from rest_framework.generics import RetrieveDestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..schemas import list_schedule_schema, create_schedule_schema

class ScheduleListAPIView(APIView):

    schema = list_schedule_schema

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
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


class ScheduleCreateAPIView(APIView):
    schema = create_schedule_schema
    def post(self, request, *args, **kwargs):
        data = request.data
        if data['daykind'] == 2:
            Schedule.objects.create(user_id=data['user'], weekday_id=data['weekday'], daykind_id=3, is_empty=True)
        if data['daykind'] == 3:
            Schedule.objects.create(user_id=data['user'], weekday_id=data['weekday'], daykind_id=2, is_empty=True)
        if data['daykind'] == 4:
            Schedule.objects.create(user_id=data['user'], weekday_id=data['weekday'], daykind_id=4, is_empty=True)
            return Response({"detail":"success"})
        serializer = PostSchedulesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response({"detail":"success"})