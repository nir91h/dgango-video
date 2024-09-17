from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from . import models

def video_page(request: HttpRequest) -> HttpResponse:
    video = models.Video.objects.get(pk=1)
    context = {'video' : video}

    return render(request, 'video.html', context)
