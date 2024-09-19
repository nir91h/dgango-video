from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from . import models

def video_page(request: HttpRequest, video_id: int) -> HttpResponse:
    video = models.Video.objects.get(pk=video_id)
    print(video.thumbnail.url)
    context = {'video' : video}

    return render(request, 'video.html', context)
