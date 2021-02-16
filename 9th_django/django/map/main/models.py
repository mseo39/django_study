from django.db import models
from imagekit.models import ImageSpaceField
from imagekit.processors import ResizeToFill
# Create your models here.

class Pictures(models.Model):
    text = models.TextField()
    image= models.ImageField(upload_to="blogimg")
    image_thumbnail = ImageSpaceField(source='image', processors=[ResizeToFill(120,60)])
    #가로 세로
    #format='JPEG' option={'quality':60}
