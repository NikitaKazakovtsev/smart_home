# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView
from measurement.models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerialaizer


class SensorListView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerialaizer

class SensorRetrieveView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class SensorCreateAPIView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerialaizer
    
class SensorPatchAPIView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerialaizer

class MeasurementAddAPIView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer