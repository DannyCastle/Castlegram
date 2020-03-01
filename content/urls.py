from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='content-home'),
    path('about/', views.about, name='content-about'),
]
