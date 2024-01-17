from django.shortcuts import render, redirect
from .forms import AppointmentForm 
from .models import Flash 
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from .models import Appointment
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'accounts/signup.html', context)

#create appointment
class AppointmentCreate(CreateView):
    model = Appointment
    fields = '__all__'

# APPOINTMENT DELETE


class AppointmentDelete(DeleteView):
    model = Appointment
    success_url = '/appointments'

