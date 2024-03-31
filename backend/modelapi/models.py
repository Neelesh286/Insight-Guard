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
class ProcessedImage(models.Model):
    uploaded_image = models.ForeignKey(UploadedImage, on_delete=models.CASCADE)
    disc_area = models.FloatField(max_length = 50)
    cup_area = models.FloatField(max_length = 50)
    cupdisc_ratio = models.FloatField(max_length = 50)
    s3_link = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Processed Image for {self.uploaded_image}"