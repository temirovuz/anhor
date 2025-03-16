from rest_framework import serializers

from employee.models import Employee, AccessTimes, DepartureTimes, WorkingDay


class WorkingDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingDay
        fields = ['id', 'date']
        extra_kwargs = {'id': {'read_only': True}}


class AccessTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessTimes
        fields = ['id', 'enter_time']
        extra_kwargs = {'id': {'read_only': True}}


class DepartureTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartureTimes
        fields = ['id', 'departure_time']
        extra_kwargs = {'id': {'read_only': True}}
