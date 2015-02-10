from django.shortcuts import render
from django.http import HttpResponse

def grooveGenerator(request):
    return HttpResponse("grooveGenerator says hey there world!")
