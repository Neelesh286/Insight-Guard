from rest_framework import serializers
from .models import UploadedImage
from PIL import Image
from pathlib import Path
from .prediction import Predict

class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ('id', 'image', 'uploaded_at','result')
    
    def validate_image(self, value):
        try:
            img = Image.open(value)
            print(f'Image is of type {value}')
        except Exception as e:
            raise serializers.ValidationError(e)
        
        valid_formats = ['PNG', 'JPEG', 'JPG']
        if img.format not in valid_formats:
            raise serializers.ValidationError("Only PNG & JPEG formats are supported")
        
        return value
    
    def create(self, validated_data):
        image = validated_data.pop('image')
        instance = UploadedImage.objects.create(image=image, **validated_data)
        # Get the path of the saved image
        saved_image_path = instance.image.path
        # Now you can pass saved_image_path to your predictor function
        # Instantiate the Predict class
        predictor = Predict()  
        saved_img = Image.open(saved_image_path)
        print(f'========={saved_image_path}=========')
        saved_image_path_obj = Path(saved_image_path)
        res   ult = predictor.prediction(saved_image_path_obj)
        print(f'MODEL PREDICTION RESULT IS => {result}')
        return instance