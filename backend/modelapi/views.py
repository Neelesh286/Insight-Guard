from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

class HelloWorldView(APIView):
    def get(self, request, format=None):
        return JsonResponse({'message': 'Hello, world!'})
