from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from ..models import TimeConfig
from rest_framework.views import APIView
from ..serializers import TimeConfigSerializer
from rest_framework.response import Response

class TimeConfigListAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        print(pk)
        time_conf = TimeConfig.objects.filter(user_id=pk).first()
        serialized = TimeConfigSerializer(time_conf)
        return Response(serialized.data)
    

class TimeConfigUpdateAPIView(UpdateAPIView): 
    queryset = TimeConfig.objects.all()
    serializer_class = TimeConfigSerializer
    

