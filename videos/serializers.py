from rest_framework.serializers import ModelSerializer

from .models import Video

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = ['video_id', 'title', 'duration', 'url', 'thumbnail']