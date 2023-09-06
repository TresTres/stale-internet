from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def index(_request: HttpRequest):
    return HttpResponse("Themes index.")