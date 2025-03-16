from django.shortcuts import get_object_or_404
from rest_framework import generics, filters
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

from employee.api.serializers import AccessTimeSerializer, WorkingDaySerializer, DepartureTimeSerializer, \
    ProductSerializer, DailyProductSerializer
from employee.models import WorkingDay, AccessTimes, DepartureTimes, Product, DailyProduction


class WorkingDayAPIView(generics.ListCreateAPIView):
    queryset = WorkingDay.objects.all()
    serializer_class = WorkingDaySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['date']

    def create(self, request, *args, **kwargs):
        date = request.data.get('date')
        if not date:
            return Response({"error": "Siz hech qanday malumot kiritmadingiz"})
        if WorkingDay.objects.filter(date=date).exists():
            return Response({'error': 'Bu sana mavjud'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)


class AccessTimeAPIView(generics.ListCreateAPIView):
    queryset = AccessTimes.objects.all()
    serializer_class = AccessTimeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['enter_time']

    def create(self, request, *args, **kwargs):
        enter_time = request.data.get('enter_time')
        if not enter_time:
            return Response({"error": "Siz hech qanday malumot kiritmadingiz"})
        if AccessTimes.objects.filter(enter_time=enter_time).exists():
            return Response({'error': 'Bu Vaqt mavjud'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)


class DepartureTimeAPIView(generics.ListCreateAPIView):
    queryset = DepartureTimes.objects.all()
    serializer_class = DepartureTimeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['departure_time']

    def create(self, request, *args, **kwargs):
        departure_time = request.data.get('departure_time')
        if not departure_time:
            return Response({"error": "Siz hech qanday malumot kiritmadingiz"})
        if DepartureTimes.objects.filter(departure_time=departure_time).exists():
            return Response({'error': 'Bu Vaqt mavjud'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)


class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        if not name:
            return Response({"error": "Siz hech qanday malumot kiritmadingiz"})
        if DepartureTimes.objects.filter(name=name).exists():
            return Response({'error': 'Bu Nomli maxsulot mavjud'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)


class DailyProductAPIView(views.APIView):
    def post(self, request):
        serializer = DailyProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        date_id = request.query_params.get('date')
        if not date_id:
            return Response({'error': 'Kerakli sanani tanlang'}, status=status.HTTP_400_BAD_REQUEST)
        working_day = get_object_or_404(WorkingDay, id=date_id)
        products = DailyProduction.objects.filter(date=working_day)
        serializer = DailyProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
