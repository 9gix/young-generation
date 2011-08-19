# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from blog.models import Entry

def blog(request):
    entries = Entry.objects.all()
    return direct_to_template(request, 'blog/index.html', {'entries':entries})