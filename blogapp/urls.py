# blogapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),         # Home page
    path('login/', views.login_view, name='login'),      # Login page
    path('register/', views.register_view, name='register'),  # Register page
    path('logout/', views.logout_view, name='logout'),  # Logout
]