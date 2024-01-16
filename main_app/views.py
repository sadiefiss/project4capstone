from django.shortcuts import render, redirect
from .forms import AppointmentForm 
from .models import Flash

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')  # Redirect to a success page or the appointment detail page
    else:
        form = AppointmentForm()
    return render(request, 'appointments/new.html', {'form': form}) 

# views.py

def home(request):
    # You can add more context or logic here as needed
    return render(request, 'home.html')  # Ensure 'home.html' exists in your templates directory



def flash_list(request):
    flashes = Flash.objects.all()  # Make sure you have a Flash model and it's imported
    return render(request, 'flash/list.html', {'flashes': flashes})