#from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path , re_path
from . import views

urlpatterns = [
    re_path('index/$' ,views.index,name='index'),
    re_path('c/$',views.challenges,name='challenges'),
    re_path('con/$',views.contact,name='contact'),
    re_path('se/$',views.seconnecter,name='seconnecter'),
    re_path('sins/$',views.sinscrire,name='sinscrire'),
    re_path('profile/$',views.profile,name='profile'),
    re_path('mecha/$',views.meschallenges,name='meschallenges'),
    re_path('m/$',views.ls,name='ls')
]