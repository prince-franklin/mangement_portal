from django.shortcuts import render, redirect
from .forms import AdditionForm, CustomLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def register(request):
    if request.method=="POST":
        form=AdditionForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, ('Registration completed'))
        return redirect('login')
    else:
        register=AdditionForm()
        return render(request, 'register.html', {'register': register})


def custom_login(request):
    if request.method == "POST":
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard') 
            else:
                messages.error(request, 'Invalid email or password')
    else:
        form = CustomLoginForm()
    
    return render(request, 'login.html', {'form': form})

    
def custom_logout(request):
        logout(request)
        return render (request, ' logout.html')
        
        
    

