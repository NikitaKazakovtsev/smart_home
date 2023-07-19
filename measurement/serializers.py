from rest_framework import serializers

from measurement.models import Measurement, Sensor


class SensorSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature']
        

class MeasurementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementDetailSerializer(read_only=True, many=True)
    
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']