from django.db import models

# Create your models here.
class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    #result = models.CharField(max_length=50)

    def __str__(self):
        return self.image.name
    
class UploadedResult(models.Model):
    uploaded_image = models.ForeignKey(UploadedImage, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

    class Meta:
        indexes = [
            models.Index(fields=['uploaded_image'])
        ]

        constraints =[
            models.UniqueConstraint(fields=['uploaded_image'], name='unique_uploaded_image_result'),
        ]