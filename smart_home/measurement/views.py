# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
import datetime
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class SensorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementCreateAPIView(generics.CreateAPIView):
    serializer_class = MeasurementSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(created_at=datetime.datetime.now())


class SensorDetailAPIView(generics.RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementImageCreateAPIView(generics.CreateAPIView):
    serializer_class = MeasurementSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        sensor_id = self.kwargs.get('sensor_id')
        sensor = Sensor.objects.get(id=sensor_id)
        serializer.save(sensor=sensor, created_at=datetime.datetime.now())
