from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import CreateClientForm
from django.contrib import messages
from .models import Contest
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    print(request.user.username)
    return render(request,'main/index.html')

def challenges(request):
    contest = Contest.objects.all()
    context = {'contest': contest}
    return render(request,'main/challenges.html',context)

def contact(request):
    return render(request,'main/contact.html')

def seconnecter(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        client = authenticate(request,username = username,password = password)
        if client is not None:
            login(request,client)
            return redirect('profile')
        else :
            messages.info(request,"Le nom d'utulisateur ou le mot de passe est inccorecte")
            return render(request,'main/seConnecter.html')
    return render(request,'main/seConnecter.html')

def sinscrire(request):
    form = CreateClientForm()
    if request.method == "POST" :
        form = CreateClientForm(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request,' votre compte est crée avec succès')
            return redirect('seconnecter')
    context = {'form' : form}
    return render(request,'main/sinscrire.html',context)

def profile(request):
    username = request.user.username
    fn = request.user.first_name
    ln = request.user.last_name
    email = request.user.email
    context = {'username' : username , "fn" : fn , "ln" : ln, "email" : email}
    return render(request,'main/profile.html',context)

def meschallenges(request):
    return render(request,'main/meschallenges.html')

def ls(request):
    if request.user.username=="admin":
        return redirect('seconnecter')
    #else




    
