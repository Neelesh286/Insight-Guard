from django.urls import path
from . import views

urlpatterns = [
    path('hello-world', views.HelloWorldView.as_view(), name='HelloWorldView'),
    path('upload/', views.UploadImageView.as_view(), name='upload_image'),
    path('result/<int:image_id>/', views.UploadedResultAPIView.as_view(),name='prediction_result')
] 