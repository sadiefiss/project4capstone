from django.shortcuts import render, redirect
from .forms import AppointmentForm 
from .models import Flash 
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .models import Appointment
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
#unsure about this
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, get_object_or_404
from .models import Appointment



def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
         
            appointment = form.save(commit=False)  # Create the appointment instance, but don't save it to the DB yet
            appointment.user = request.user  # Assign the logged-in user   
            appointment.save()
            return redirect('appointment_success')  # Redirect to a success page or the appointment detail page
    else:
        form = AppointmentForm()
    return render(request, 'appointments/new.html', {'form': form}) 
#appointment sucsess
# views.py

def appointment_success(request):
    # Your view logic here
    return render(request, 'appointments/success.html')


#appointment index
def appointments_index(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/index.html', {'appointments': appointments})


# views.py

#appointment detail

def appointment_detail(request, appointment_id):
    # Retrieve an Appointment object by id or return a 404 error if not found
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    
    # Make sure the logged-in user is the owner of the appointment
    if request.user != appointment.user:
        return render(request, 'errors/403.html'), 403
    
    # Render the appointment details template with the appointment context
    return render(request, 'appointments/detail.html', {'appointment': appointment})


def home(request):
    # You can add more context or logic here as needed
    return render(request, 'home.html')  # Ensure 'home.html' exists in your templates directory


@login_required
def flash_list(request):
    flashes = Flash.objects.filter(appointment__user=request.user) #  updated step 10 Make sure you have a Flash model and it's imported
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
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'accounts/signup.html', context)

#create appointment
# class AppointmentCreate(CreateView):
#     model = Appointment
#     fields = '__all__'

class AppointmentCreate(LoginRequiredMixin, CreateView):
    model = Appointment
    fields = ['date', 'flash', 'notes']  # Specify the fields you want the user to fill out
    success_url = '/appointments'  # Adjust this to wherever you want users to go after creating an appointment

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the logged-in user to the appointment
        return super().form_valid(form)

# APPOINTMENT DELETE


class AppointmentDelete(DeleteView):
    model = Appointment
    success_url = '/appointments'

#update view
class AppointmentUpdate(UpdateView):
    model = Appointment
    fields = ['date', 'flash', 'notes']
