from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['user', 'date', 'flash', 'notes']
        # Add any other fields from your Appointment model here
