from django.urls import path
from . import views

urlpatterns = [
    path('hello-world', views.HelloWorldView.as_view(), name='HelloWorldView'),
]