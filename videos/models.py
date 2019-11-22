from django.db import models

class Video(models.Model):
     video_id = models.CharField(
          max_length=30,
          primary_key=True
     )
     title = models.TextField()
     duration = models.DurationField()
     url = models.URLField()
     thumbnail = models.TextField()
