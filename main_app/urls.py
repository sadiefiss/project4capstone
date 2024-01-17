from django.urls import path 
from django.contrib.auth import views as auth_views  # Import Django's authentication views
from . import views
from .views import AppointmentCreate


urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('flashes/', views.flash_list, name='flashes'),  # Again, ensure the name matches
    path('', views.home, name='home'),  # Define the root URL
    # ... any other URL patterns you have ...
    # Add login and logout URLs using Django's built-in views
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # ... any other URL patterns you have ...
    path('appointment/create/', AppointmentCreate.as_view(), name='appointment_create'),
    path('appointment/<int:pk>/delete/', views.AppointmentDelete.as_view(), name='appoointment_delete'),
# New url pattern below
    path('accounts/signup/', views.signup, name='signup'),
]



