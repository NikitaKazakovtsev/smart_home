from django.urls import path

from measurement.views import MeasurementAddAPIView, SensorCreateAPIView, SensorListView, SensorPatchAPIView, SensorRetrieveView

urlpatterns = [
    path('sensors_list/', SensorListView.as_view(), name = 'sensors_list'),
    path('sensors_id/<pk>/', SensorRetrieveView.as_view(), name = 'sensors_id'),
    path('sensors_create/', SensorCreateAPIView.as_view(), name = 'sensors_create'),
    path('sensors_change/<pk>/', SensorPatchAPIView.as_view(), name = 'sensors_change'),
    path('measurements_add/', MeasurementAddAPIView.as_view(), name = 'sensors_change'),

]

