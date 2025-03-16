from rest_framework import serializers

from employee.models import Employee, AccessTimes, DepartureTimes, WorkingDay, Product, DailyProduction


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


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price_per_unit']
        extra_kwargs = {'id': {'read_only': True}}


class DailyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyProduction
        fields = ['id', 'date', 'product', 'total_quantity']
        extra_kwargs = {'id': {'read_only': True}}
