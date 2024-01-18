from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views  # Import Django's authentication views
from . import views
from .views import AppointmentCreate, AppointmentUpdate, AppointmentDelete 
from django.conf import settings
from django.conf.urls.static import static


# urlpatterns = [
#     path('book/', views.book_appointment, name='book_appointment'),
#     path('flashes/', views.flash_list, name='flashes'),  # Again, ensure the name matches
#     path('', views.home, name='home'),  # Define the root URL
#     # ... any other URL patterns you have ...
#     # Add login and logout URLs using Django's built-in views
#     path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
#     # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     # path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
#     # ... any other URL patterns you have ...
#     path('appointment/create/', AppointmentCreate.as_view(), name='appointment_create'),
#     path('appointment/<int:pk>/delete/', views.AppointmentDelete.as_view(), name='appoointment_delete'),
# # New url pattern below
# #index
#     path('appointments/', views.appointments_index, name='appointments_index'),
#     path('appointment/success/', views.appointment_success, name='appointment_success'),
#     path('accounts/signup/', views.signup, name='signup'),
#     #appointment detail
#     path('appointments/<int:appointment_id>/', views.appointment_detail, name='appointment_detail'),
#    #path('appointments/<int:appointment_id>/edit/', views.appointments_update, name='appointments_update'),
#     path('appointments/<int:appointment_id>/delete/', views.appointments_delete, name='appointments_delete'),
#     path('appointments/<int:pk>/edit/', AppointmentUpdate.as_view(), name='Appointmentpdate')
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path('', views.home, name='home'),  # Root URL
    path('book/', views.book_appointment, name='book_appointment'),
    path('flashes/', views.flash_list, name='flashes'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # Uncomment and correct the following line if you have a logout view
    # path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
    path('appointment/create/', AppointmentCreate.as_view(), name='appointment_create'),
    path('appointment/<int:pk>/delete/', AppointmentDelete.as_view(), name='appointment_delete'),
    path('appointments/', views.appointments_index, name='appointments_index'),
    path('appointment/success/', views.appointment_success, name='appointment_success'),
    path('accounts/signup/', views.signup, name='signup'),
    path('appointments/<int:appointment_id>/', views.appointment_detail, name='appointment_detail'),
    # Make sure the following line points to an existing view or is removed
    # path('appointments/<int:appointment_id>/delete/', views.appointments_delete, name='appointments_delete'),
    path('appointments/<int:pk>/edit/', AppointmentUpdate.as_view(), name='appointment_update'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

