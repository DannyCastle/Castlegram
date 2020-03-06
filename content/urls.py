from . import views
from django.urls import path
from users import views as users_views

urlpatterns = [
    path('', views.home, name='content-home'),
    path('about/', views.about, name='content-about'),
    path('register/', users_views.register, name='register'),
]
