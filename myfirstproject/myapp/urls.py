
from django.urls import path
from .import views


urlpatterns = [
     path('',views.AllCars,name='AllCars'),
     path('car/<int:car_id>/',views.Car_des,name='car_details'),
     path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
  
]