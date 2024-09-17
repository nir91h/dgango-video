from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def video_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse('This is video')
