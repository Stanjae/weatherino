
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.weatherinfo , name='weatherinfo'),
     path('delete/<str:pk>/', views.deleteweather , name='deleteinfo')
]