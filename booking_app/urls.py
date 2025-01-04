from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('booking/<uuid:booking_id>/', views.get_booking_details, name='get_booking_details'),
    
]