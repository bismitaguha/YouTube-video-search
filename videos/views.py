import requests
import threading
import json

from isodate import parse_duration

from django.conf import settings
from django.shortcuts import render, redirect  
from .models import Videos

def index(request):
    videos = []

    if request.method == 'GET':
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'

        search_params = {
            'part' : 'snippet',
            'q' : 'nobody',
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'order' : 'date',
            'maxResults' : 25,
            'type' : 'video'
        }

        r = requests.get(search_url, params=search_params)

        results = r.json()['items']

        video_ids = []
        for result in results:
            video_ids.append(result['id']['videoId'])

        video_params = {
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'part' : 'snippet,contentDetails',
            'id' : ','.join(video_ids),
            'order' : 'date',
            'maxResults' : 25
        }

        r = requests.get(video_url, params=video_params)

        results = r.json()['items']

        for result in results:         
            video_data = {
                'title' : result['snippet']['title'],
                'video_id' : result['id'],
                'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
                'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                'thumbnail' : result['snippet']['thumbnails']['high']['url']
            }
            videos.append(video_data)

            v = Videos(
                title = result['snippet']['title'],
                video_id = result['id'],
                url = f'https://www.youtube.com/watch?v={ result["id"] }',
                duration = int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                thumbnail = result['snippet']['thumbnails']['high']['url']
            )
            v.save()
            

    context = {
        'videos' : videos
    }
    
    return render(request, 'search/index.html', context)