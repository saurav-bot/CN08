from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
import requests

@login_required
def home(request):
    return render(request, "home.html")

def post_fetch(request):
    limit=request.GET.get('limit')
    start=request.GET.get('start')
    response = requests.get("https://api.github.com/users/saurav-bot/events").json()
    response_list = response[int(start):int(start)+int(limit)]
    context={
        "data":response_list,
        "avatar":response[0]["actor"]['avatar_url']
    }

    return render(request, "result.html", context)