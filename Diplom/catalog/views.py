from django.shortcuts import render
import asyncio
from django.http import HttpResponse
from .models import Games
import requests
from bs4 import BeautifulSoup

def index(request):


    sas = Games.objects.all()
    print(sas)
    san = []
    url = 'https://gabestore.ru'
    model = Games()
    async def quest():
        pass

    return render(request, "index.html", )#context={'num': [0]*len(soup), 'san': san,'soup': soup, 'info': info, })

def game(request):

    return render(request, "tovar.html", )  # context={'num': [0]*len(soup), 'san': san,'soup': soup, 'info': info, })