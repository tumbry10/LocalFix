from django.shortcuts import render, redirect
from accounts.decorators import role_required
from django.contrib.auth.decorators import login_required
from .models import Service, Booking

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def service_list(request):
    services = Service.objects.all()
    context =  {
        'services': services
    }
    return render(request, 'main/service_list.html', context)

@login_required
@role_required('provider')
def provider_dashboard(request):
    my_services = Service.objects.filter(provider=request.user)
    my_bookings = Booking.objects.filter(service__provider=request.user)

    context = {
        'services': my_services,
        'bookings': my_bookings,
    }
    return render(request, 'main/provider_dashboard.html', context)

@login_required
@role_required('seeker')
def seeker_dashboard(request):
    my_bookings = Booking.objects.filter(seeker=request.user)

    context = {
        'bookings': my_bookings,
    }
    return render(request, 'core/seeker_dashboard.html', context)

@login_required
@role_required('provider')
def add_service(request):
    if request.method == 'POST':
        # Handle form data here (we'll build this in the next step)
        pass
    return render(request, 'core/add_service.html')