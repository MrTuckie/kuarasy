from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def panel_view(request):
    return HttpResponse("<h1>kûarasy</h1>")
