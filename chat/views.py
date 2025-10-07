from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("Hello. You're at the chat view.")
