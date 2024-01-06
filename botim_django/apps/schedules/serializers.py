#model 
from .models import WeekDay, Schedule, DayKind, TimeConfig
#rest_framework
from rest_framework.serializers import ModelSerializer
#parler
from django.utils.translation import get_language_from_path
from parler_rest.serializers import TranslatableModelSerializer



class TimeConfigSerializer(ModelSerializer):
     class Meta:
          model = TimeConfig
          fields = '__all__'

class GetWeekDaySerializer(TranslatableModelSerializer):
    class Meta:
        model = WeekDay
        fields = ['id', 'name']

    def to_representation(self, instance):
            language = get_language_from_path(self.context['request'].path)
            instance.set_current_language(language)
            return super().to_representation(instance)
        

class GetDayKindSerializer(TranslatableModelSerializer):
    class Meta:
        model = DayKind
        fields = ['id', 'name']

    def to_representation(self, instance):
            language = get_language_from_path(self.context['request'].path)
            instance.set_current_language(language)
            return super().to_representation(instance)
    

class GetSchedulesSerializer(ModelSerializer):
    weekday = GetWeekDaySerializer()
    daykind = GetDayKindSerializer()
    class Meta:
        model = Schedule
        fields = '__all__'


class PostSchedulesSerializer(ModelSerializer):
    # weekday = GetWeekDaySerializer(read_only=True)
    # daykind = GetDayKindSerializer(read_only=True)
    class Meta:
        model = Schedule
        fields = '__all__'
        

