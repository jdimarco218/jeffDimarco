# coding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from datetime import datetime

def home(request):
    context = RequestContext(request)
    return render_to_response('core/home.html', context)

def about(request):
    context = RequestContext(request)
    return render_to_response('core/about.html', context)
