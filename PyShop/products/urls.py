from django.urls import path
# 'from .' significa a pasta atual
from . import views


urlpatterns = [
    path('', views.index),
    path('new/', views.new),
]