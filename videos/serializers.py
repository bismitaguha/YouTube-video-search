from rest_framework import serializers

class VideoSerializer(serializers.Serializer):
    video_id = serializers.CharField(max_length=30)
    title = serializers.CharField()
    duration = serializers.IntegerField()
    url = serializers.CharField()
    thumbnail = serializers.CharField()