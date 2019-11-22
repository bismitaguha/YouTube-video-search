from django.urls import path
from videos.views import ListVideo

urlpatterns = [
    path('', ListVideo.as_view({'get': 'list'})),
]