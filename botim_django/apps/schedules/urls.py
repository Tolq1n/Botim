from django.contrib import admin
from django.urls import path, include
from .views.week_day import WeekDayRetrieveAPIView, WeekDayListAPIView
from .views.day_kind import DayKindRetrieveAPIView, DayKindListAPIView
from .views.time_conf import TimeConfigListAPIView, TimeConfigUpdateAPIView
from .views.schedules import ScheduleRetrieveDestroyAPIView, ScheduleUpdateAPIView, ScheduleCreateAPIView, ScheduleListAPIView

urlpatterns = [
    #week_day
    # path('week_days/<int:pk>', WeekDayRetrieveAPIView.as_view()),
    # path('week_days/list', WeekDayListAPIView.as_view()),

    #day_kind
    # path('day_kind/<int:pk>', DayKindRetrieveAPIView.as_view()),
    # path('day_kind/list', DayKindListAPIView.as_view()),

    #time config
    path('time-conf/<int:pk>', TimeConfigListAPIView.as_view()),
    path('time-conf/update/<int:user_id>', TimeConfigUpdateAPIView.as_view()),

    #schedule
    path('<int:pk>', ScheduleRetrieveDestroyAPIView.as_view()),
    path('update/<int:pk>', ScheduleUpdateAPIView.as_view()),
    path('list/', ScheduleListAPIView.as_view()),
    path('create', ScheduleCreateAPIView.as_view()),
]
