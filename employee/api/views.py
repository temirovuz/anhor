from rest_framework import generics

from employee.api.serializers import AccessTimeSerializer, WorkingDaySerializer, DepartureTimeSerializer
from employee.models import WorkingDay, AccessTimes, DepartureTimes


class WorkingDayAPIView(generics.ListCreateAPIView):
    queryset = WorkingDay.objects.all()
    serializer_class = WorkingDaySerializer


class AccessTimeAPIView(generics.ListCreateAPIView):
    queryset = AccessTimes.objects.all()
    serializer_class = AccessTimeSerializer


class DepartureTimeAPIView(generics.ListCreateAPIView):
    queryset = DepartureTimes.objects.all()
    serializer_class = DepartureTimeSerializer
