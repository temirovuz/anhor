from rest_framework import generics

from employee.api.serializers import AccessTimeSerializer, WorkingDaySerializer, DepartureTimeSerializer, \
    ProductSerializer
from employee.models import WorkingDay, AccessTimes, DepartureTimes, Product


class WorkingDayAPIView(generics.ListCreateAPIView):
    queryset = WorkingDay.objects.all()
    serializer_class = WorkingDaySerializer


class AccessTimeAPIView(generics.ListCreateAPIView):
    queryset = AccessTimes.objects.all()
    serializer_class = AccessTimeSerializer


class DepartureTimeAPIView(generics.ListCreateAPIView):
    queryset = DepartureTimes.objects.all()
    serializer_class = DepartureTimeSerializer


class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
