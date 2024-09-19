from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from video import models

def home_page(request: HttpRequest) -> HttpResponse:
    videos = models.Video.objects.all()
    context = {'videos': videos}
    return render(request, 'main/index.html', context)
