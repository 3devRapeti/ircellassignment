from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import profiles
from django.template import loader

def hello(request):
   all_albums = profiles.objects.all()
   template = loader.get_template('website/outbound.html')
   context = {
       'all_albums': all_albums,
   }
   return HttpResponse(template.render(context, request))