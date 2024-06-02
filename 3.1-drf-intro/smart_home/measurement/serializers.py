from rest_framework import serializers
from .models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы

class MeasurementSer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'


class SensorSer(serializers.ModelSerializer):
    measurements = MeasurementSer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'desc', 'measurements']


