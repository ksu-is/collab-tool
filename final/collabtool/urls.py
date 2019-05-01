from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tool-home'),
    path('about/', views.about, name='tool-about'),
]