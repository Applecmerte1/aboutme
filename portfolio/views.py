from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def blog(request):
    projects = Project.objects.all()
    return render(request, 'blog.html', {'projects':projects})