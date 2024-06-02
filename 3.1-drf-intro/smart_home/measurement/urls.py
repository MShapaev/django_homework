from django.urls import path, include
from .views import SensorViewSet, MeasurementsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('sensors', SensorViewSet)
router.register('measurements', MeasurementsViewSet)

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    
    path('api/', include(router.urls)),
]
