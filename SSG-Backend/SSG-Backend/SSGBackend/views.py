from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import get_resolver
import json

# Create your views here.

#index-/landing-site
def index(request):
    overview()
    return HttpResponse(overview())

#overview about
def overview():
    site_collection = {}
    my_urls = get_resolver().url_patterns
    print(type(my_urls))
    print(my_urls[0])
    print(my_urls[1])
    print(len(my_urls))
    for i in len(my_urls):
        print(i)
    
    
    site_collection = json.dumps(site_collection)
    #print(type(json.loads(site_collection)))
    return site_collection
