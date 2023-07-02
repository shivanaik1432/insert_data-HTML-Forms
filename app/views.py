from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *

def insert_topic(request):
    if request.method=='POST':
        topic=request.POST['tp']
        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('Topic is inserted')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    TO=Topic.objects.all()
    d={'TO':TO}
    if request.method=='POST':
        topic=request.POST['tp']
        name=request.POST['name']
        url=request.POST['url']
        email=request.POST['email']

        TOF=Topic.objects.get(topic_name=topic)
        WO=Webpage.objects.get_or_create(topic_name=TOF,name=name,url=url,email=email)[0]
        WO.save()
        return HttpResponse('Webpage is inserted')

    return render(request,'insert_webpage.html',d)