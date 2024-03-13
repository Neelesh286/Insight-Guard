from django.urls import path
from . import views

urlpatterns = [
    path('hello-world', views.HelloWorldView.as_view(), name='HelloWorldView'),
    path('upload/', views.UploadImageView.as_view(), name='upload_image'),
] 