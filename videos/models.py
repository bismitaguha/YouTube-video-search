from django.db import models

from django.conf import settings

# Create your models here.

class Videos(models.Model):
     video_id = models.CharField(max_length=30, null=False, primary_key=True)
     title = models.TextField(null=False)
     duration = models.IntegerField()
     url = models.TextField()
     thumbnail = models.TextField()
    
