from django.shortcuts import render
from django.conf import settings
import json
import os

# Create your views here.
def index(request):
    data = json.load(open(os.path.join(settings.BASE_DIR, 'data.json')))
    context={
        "about": data['about'],
        "social_media": data['social_media'],
        "skills":data['skills'],
        "services":data['services'],
        "developer": data['developers']
    }
    name = "s"
    # print(name.upper())
    print(data['about'])
    return render(request, 'main/index.html', context)

# def projects(request):
#     context={}
#     return render(request, 'main/projects.html', context)