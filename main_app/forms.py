from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [ 'date', 'flash', 'notes']
        # Add any other fields from your Appointment model here
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # HTML5 date-picker
        }
