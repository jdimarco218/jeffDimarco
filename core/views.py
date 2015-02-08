# coding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from reviews.models import Review
from activities.models import Activity
from datetime import datetime

def get_following_feeds(user):

def home(request):
    context = RequestContext(request)
    return render_to_response('core/cover.html', context)

def about(request):
    context = RequestContext(request)
    return render_to_response('core/about.html', context)
