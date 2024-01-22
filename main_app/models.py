# from datetime import timezone
from django.db import models
from django.contrib.auth.models import User

class Flash(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='flashes')
    description = models.TextField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)  # Date field
    time = models.TimeField(null=True, blank=True)  # Time field, can be null
    flash = models.ForeignKey(Flash, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField()

    def __str__(self):
        # Format date and time separately and handle the possibility of null values
        date_str = self.date.strftime('%Y-%m-%d') if self.date else 'No date set'
        time_str = self.time.strftime('%H:%M') if self.time else 'No time set'
        return f"Appointment for {self.user.username} on {date_str} at {time_str}"


