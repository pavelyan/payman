from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from datetime import datetime, timedelta
from django.utils import timezone
from .models import *
from django.db.models import Q
from django_tables2 import RequestConfig
from .tables import RequestTable
from django.db.models import Sum
from .utils import requests_table

# Create your views here.

managers=settings.POWER_USERS_GROUP

@login_required
def all_requests(request):  
    if request.user.groups.filter(name__contains = managers):
        qset = Request.objects.all().order_by('date_planned')
    else:
        qset=Request.objects.filter(author__username=request.user).order_by('date_planned')
    return requests_table(request, qset, 'Все заявки')


@login_required
def actual_requests(request):
    if request.user.groups.filter(name__contains = managers):
        qset = Request.objects.filter(Q(status='N') | Q(status='P')).order_by('date_planned')
    else:
        qset=Request.objects.filter(author__username=request.user).filter(Q(status='N') | Q(status='P')).order_by('date_planned')
    return requests_table(request, qset, 'Открытые заявки')


@login_required
def payed_requests(request):
    if request.user.groups.filter(name__contains = managers):
        qset = Request.objects.filter(status='Y').order_by('date_planned')
    else:
        qset=Request.objects.filter(author__username=request.user).filter(status='Y').order_by('date_planned')
    return requests_table(request, qset, 'Оплаченные заявки')


@login_required
def overdue_requests(request):
    if request.user.groups.filter(name__contains = managers):
        qset = Request.objects.filter(date_planned__lt=timezone.now()-timedelta(days=1)).filter(status='N').order_by('date_planned')
    else:
        qset=Request.objects.filter(author__username=request.user).filter(date_planned__lt=timezone.now()-timedelta(days=1)).filter(status='N').order_by('date_planned')
    return requests_table(request, qset, 'Просроченные заявки')
