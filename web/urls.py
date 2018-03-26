from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^summoner/', views.summoner, name='summoner'),
    url(r'^partidas/', views.partidas, name='partidas')
]
