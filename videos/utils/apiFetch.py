import requests
import threading
import json
from datetime import timedelta

from isodate import parse_duration
from django.conf import settings
from django.shortcuts import render, redirect

from videos.models import Video


def apiFetch(f_stop):
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'

    search_params = {
        'part' : 'snippet',
        'q' : 'nobody',
        'key' : settings.YOUTUBE_DATA_API_KEY,
        'order' : 'date',
        'type' : 'video'
    }

    r = requests.get(search_url, params=search_params)

    results = r.json()['items']

    video_ids = []
    for result in results:
        video_ids.append(result['id']['videoId'])

    query_params = {
        'key' : settings.YOUTUBE_DATA_API_KEY,
        'part' : 'snippet,contentDetails',
        'id' : ','.join(video_ids),
        'order' : 'date'
    }

    r = requests.get(video_url, params=query_params)

    results = r.json()['items']

    videos = []
    for result in results:         
        videos.append(
            Video(
                title = result['snippet']['title'],
                video_id = result['id'],
                url = f'https://www.youtube.com/watch?v={ result["id"] }',
                duration = timedelta(
                    seconds=parse_duration(result['contentDetails']['duration']).total_seconds()
                ),
                thumbnail = result['snippet']['thumbnails']['high']['url']
            )
        )
    Video.objects.bulk_create(videos, ignore_conflicts=True)

    if not f_stop.is_set():
        threading.Timer(10,apiFetch,[f_stop]).start()
