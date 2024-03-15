from rest_framework import serializers
from .models import UploadedImage
from PIL import Image
from .prediction import Predict

class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ('id', 'image', 'uploaded_at')
    
    def validate_image(self,value):
        try:
            img = Image.open(value)
            print(f'Image is of type {value}')
            predictor = Predict()  # Instantiate the Predict class
            result = predictor.prediction(img)
            print('===============', result, sep='\n')
        except Exception as e:
            raise serializers.ValidationError(e)
        
        valid_formats = ['PNG', 'JPEG', 'JPG']
        if img.format not in valid_formats:
            raise serializers.ValidationError("Only PNG & JPEG formats are supported")
        
        return value
    
    def create(self, validated_data):
        image = validated_data.pop('image')
        instance = UploadedImage.objects.create(image= image, **validated_data)
        return instance