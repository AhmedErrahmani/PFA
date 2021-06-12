from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import CreateClientForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def challenges(request):
    return render(request,'main/challenges.html')

def contact(request):
    return render(request,'main/contact.html')

def seconnecter(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        client = authenticate(request,username = username,password = password)
        if client is not None:
            login(request,client)
            return redirect('index')
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

    
