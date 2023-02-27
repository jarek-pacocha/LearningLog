"""Defines URL patterns for the users app."""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Add default URL paths to authenticate.
    path('', include('django.contrib.auth.urls')),
    # Register page.
    path('register/', views.register, name='register'),
]
