from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('track/', views.track, name='track'),
    path('quote/', views.get_quote, name='get_quote'),
]