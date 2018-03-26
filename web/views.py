from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests
import json
import os
from .models import Login

# Create your views here.

def index(request):
    return render(request, 'visual/inicio.html')

def partidas(request):
    return render(request, 'visual/index.html')

lista = [['img/3157.png','img/3040.png','img/3151.png','img/3157.png'],['img/3157.png','img/3040.png','img/3151.png','img/3157.png'],['img/3157.png','img/3040.png','img/3151.png','img/3157.png']]

diccio = [{"invo1":"img/3157.png","invo2":"img/3040.png"},{"invo1":"img/3157.png","invo2":"img/3040.png"}]
def summoner(invocador):
    if invocador.method == "POST":
        # Url para solicitar el ProfileIconId y Id del invocador
        NameSummoner = invocador.POST ["invocador"]
        UrlBase = "https://la1.api.riotgames.com"
        EndPoint = "/lol/summoner/v3/summoners/by-name/"
        ApiKey = "RGAPI-6f7074d3-4f37-4535-b469-56eddbeec88c"
        Url = UrlBase + EndPoint + NameSummoner + "?api_key=" + ApiKey
        Response = requests.get(Url).json()

        # Url para mostrar la imagen
        # UrlBaseImg = "http://ddragon.leagueoflegends.com/cdn/8.5.2/img/profileicon/"
        # UrlImagen = UrlBaseImg + str(Imagen) + ".png"


        return render(invocador, 'visual/prueba.html', {"link": Response, "imgs": lista, "mges": diccio } )
    else:
        return render(invocador, 'visual/prueba.html')

#https://la1.api.riotgames.com/lol/summoner/v3/summoners/by-name/laserspartan?api_key=RGAPI-e5889859-3f14-4b47-ae7e-cedcf672477e

#http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/1001.png
#http://ddragon.leagueoflegends.com/cdn/8.6.1/img/spell/SummonerFlash.png
#http://ddragon.leagueoflegends.com/cdn/8.6.1/img/spell/FlashFrost.png
#http://ddragon.leagueoflegends.com/cdn/8.6.1/img/passive/Aatrox_Passive.png
#http://ddragon.leagueoflegends.com/cdn/8.6.1/img/champion/Aatrox.png
#http://ddragon.leagueoflegends.com/cdn/8.6.1/img/profileicon/588.png
#http://ddragon.leagueoflegends.com/cdn/img/champion/loading/Aatrox_0.jpg
#http://ddragon.leagueoflegends.com/cdn/img/champion/splash/Aatrox_0.jpg
#http://ddragon.leagueoflegends.com/cdn/img/champion/tiles/aatrox_0.jpg
#https://lan.leagueoflegends.com/es/featured/preseason-update/8000-8008?build=01012227
