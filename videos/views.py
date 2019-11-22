import requests
import threading
import json

from django.conf import settings
from django.shortcuts import render, redirect  
from .models import Videos
from .pagination import PagesPagination
from .serializers import VideoSerializer
from rest_framework.generics import ListAPIView
from rest_framework import serializers

from .utils.apiFetch import apiFetch

class listVideo(ListAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer
    pagination_class = PagesPagination

    def list(self, request):
        apiFetch(threading.Event())

        queryset = self.get_queryset()
        serializer = VideoSerializer(queryset, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)
