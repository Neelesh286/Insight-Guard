from rest_framework.views import APIView
# from rest_framework.response import Response
from django.http import JsonResponse

# import json
# import numpy as np
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from PIL import Image
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

class HelloWorldView(APIView):
    def get(self, request, format=None):
        return JsonResponse({'message': 'Hello, world!'})


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UploadedImage
from .serializers import UploadedImageSerializer
from rest_framework.views import APIView

class UploadImageView(APIView):
    def post(self,request, *args, **kwargs):
        serializer = UploadedImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def get(self,request, *args, **kwargs):
    # Use @GET METHOD TO FETCH THE RESULT 