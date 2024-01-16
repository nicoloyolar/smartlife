from django.shortcuts import render, redirect
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('inicio') 
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def inicio_view(request):
    return render(request, 'inicio.html')
