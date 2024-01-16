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
    date = models.DateTimeField()
    flash = models.ForeignKey(Flash, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField()

    def __str__(self):
        return f"Appointment for {self.user.username} on {self.date.strftime('%Y-%m-%d %H:%M')}"
