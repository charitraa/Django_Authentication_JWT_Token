from django.contrib import admin
from django.urls import path
from Api import views

urlpatterns = [
    path('register/',views.UserRgistrationView.as_view(),name='register'),
    path('login/',views.USerLoginView.as_view(),name='register')
]
