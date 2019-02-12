from .models import *
from rest_framework import serializers
from graphene_django.rest_framework.mutation import SerializerMutation

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model=Day
        fields = '__all__'

class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Period
        fields = '__all__'

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Block
        fields = '__all__'

class RoomNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model=RoomNumber
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields = '__all__'

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Availability
        fields = '__all__'