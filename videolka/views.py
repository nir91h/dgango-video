from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def home_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Универ - Каловая общага - Смотреть онлайн ")
