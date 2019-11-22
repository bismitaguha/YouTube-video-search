import threading

from rest_framework.viewsets import ModelViewSet

from .pagination import PagesPagination
from .models import Video
from .serializers import VideoSerializer
from .utils.apiFetch import apiFetch

class ListVideo(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    pagination_class = PagesPagination
    http_method_names = ['get']

    def list(self, request):
        apiFetch(threading.Event())
        return super().list(request)
