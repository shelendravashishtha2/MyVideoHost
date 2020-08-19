from django.http import HttpResponse
from .models import Subject,Video
from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request,'csed/iframe.html')

def dbms(request):
    subject = Subject.objects.get(pk=1)
    return render(request,'csed/main.html',{'subject':subject})
def da(request):
    subject = Subject.objects.get(pk=4)
    return render(request, 'csed/main.html', {'subject': subject})
def ml(request):
    subject = Subject.objects.get(pk=3)
    return render(request,'csed/main.html',{'subject':subject})
def cd(request):
    subject = Subject.objects.get(pk=2)
    return render(request, 'csed/main.html', {'subject': subject})
def daa(request):
    subject = Subject.objects.get(pk=5)
    return render(request,'csed/main.html',{'subject':subject})