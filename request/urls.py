from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all_requests, name='all_requests'),
    path('actual/', views.actual_requests, name='actual_requests'),
    path('payed/', views.payed_requests, name='payed_requests'),
    path('overdue/', views.overdue_requests, name='overdue_requests'),
]