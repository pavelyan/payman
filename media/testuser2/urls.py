from django.urls import path
from . import views

urlpatterns = [
    path('new', views.new_record, name='new_record'),
]
