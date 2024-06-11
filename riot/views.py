from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv
from django.http import HttpResponse,JsonResponse
load_dotenv()
def index(request):
    url = 'https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/ra1nfallz/ASAP'
    API_KEY = os.getenv("API_KEY")
    headers = {
            "X-Riot-Token": API_KEY
            }
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data,safe=False)
