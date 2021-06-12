#from django.contrib import admin
from django.urls import path , re_path
from . import views

urlpatterns = [
    re_path('index/$' ,views.index,name='index'),
    re_path('c/$',views.challenges,name='challenges'),
    re_path('con/$',views.contact,name='contact'),
    re_path('se/$',views.seconnecter,name='seconnecter'),
    re_path('sins/$',views.sinscrire,name='sinscrire')
]