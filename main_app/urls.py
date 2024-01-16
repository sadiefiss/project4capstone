from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('flashes/', views.flash_list, name='flashes'),  # Again, ensure the name matches
    path('', views.home, name='home'),  # Define the root URL
    # ... any other URL patterns you have ...
]
