from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index),
    path('home', index, name='home'),
    path('srch/', views.srch),
    path('full_text', full_text, name='full_text'),
]