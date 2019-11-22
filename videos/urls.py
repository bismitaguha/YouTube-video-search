from django.urls import path
from . import views

urlpatterns = [
    path('', views.listVideo.as_view()),
]