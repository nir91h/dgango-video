from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

def login_view(request : HttpRequest) -> HttpResponse:
    if request.method == "POST":
        return redirect('/')

    return render(request, 'login/login.html')


def register(request: HttpRequest) -> HttpResponse:
    return render(request, 'login/register.html')

