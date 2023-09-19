from django.urls import path
from . import views

urlpatterns = [
    path('sensors/', views.SensorListCreateAPIView.as_view(), name='sensor-list-create'),
    path('sensors/<int:pk>/', views.SensorRetrieveUpdateAPIView.as_view(), name='sensor-retrieve-update'),
    path('sensors/<int:sensor_id>/measurements/', views.MeasurementCreateAPIView.as_view(), name='measurement-create'),
    path('sensors/<int:sensor_id>/', views.SensorDetailAPIView.as_view(), name='sensor-detail'),
    path('sensors/<int:sensor_id>/measurements/image/', views.MeasurementImageCreateAPIView.as_view(),
         name='measurement-image-create'),
]
