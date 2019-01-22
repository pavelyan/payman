from django.urls import path
from . import views

urlpatterns = [
    path('', views.requests_list, name='requests_list'),
]