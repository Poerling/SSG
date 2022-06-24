from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests

# Create your views here.

#index-/landing-site
def index(request):
    context = {0:'/index',
               1:'/home',
               2:'/fussballde',
               3:'/dummy3'}
    return render(request,"SSGBackend/index.html", {"context":context})


#fussballde widget
def fussballde(request):
    get_request = requests.get('https://www.fussball.de/widget2/-/schluessel/02IF7N66TC000000VUM1DNOHVURP64MN/target/widget1/caller/localhost%3A8000#!/')
    start_string = str(get_request.text)
    print(start_string.find('<table class="table table-striped table-full-width">'))
    context = {'message':'Fussball.de Widget (only for testing)',
               'request':get_request.text}
    return render(request,"SSGBackend/fussballde.html", {"context":context})
