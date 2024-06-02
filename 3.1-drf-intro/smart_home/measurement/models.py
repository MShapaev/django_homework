from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):

    name = models.CharField(max_length=100, verbose_name='Название')
    desc = models.CharField(max_length=100, verbose_name='Описание')


class Measurement(models.Model):

    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temp = models.IntegerField()
    date = models.DateField(auto_now_add=True)