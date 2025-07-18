from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import ProviderRegisterForm, SeekerRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
def register_provider(request):
    if request.method == 'POST':
        form = ProviderRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('provider_dashboard')
    else:
        form = ProviderRegisterForm()
    context =  {
        'form': form,
        'role': 'Service Provider'
    }
    return render(request, 'accounts/register.html', context)

def register_seeker(request):
    if request.method == 'POST':
        form = SeekerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('seeker_dashboard')
    else:
        form = SeekerRegisterForm()
    context = {
        'form': form,
        'role': 'Service Seeker'
    }
    return render(request, 'accounts/register.html', context)