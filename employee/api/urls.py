from django.urls import path

from employee.api.views import WorkingDayAPIView, AccessTimeAPIView, DepartureTimeAPIView

urlpatterns = [
    path('working-day/', WorkingDayAPIView.as_view(), name='workingday-create-list'),
    path('access-time/', AccessTimeAPIView.as_view(), name='access-time-create-list'),
    path('departure-time/', DepartureTimeAPIView.as_view(), name='departure-time-create-list'),
]
