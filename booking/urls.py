from django.urls import path

# from .views.main import index, ReservationCreate, ReservationUpdate
from .import views

urlpatterns = [
 
    path('booking', views.booking, name='book'),
]