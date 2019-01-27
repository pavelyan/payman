from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from datetime import datetime, timedelta
from django.utils import timezone
from .models import *
from django.db.models import Q

# Create your views here.

@login_required
def all_requests(request):
    managers=settings.POWER_USERS_GROUP
    if request.user.groups.filter(name__contains = managers):
        r_list=Request.objects.all().order_by('date_planned')
        scope='Все заявки ({})'.format(str(r_list.count())) 
    else:
        r_list=Request.objects.filter(author__username=request.user).order_by('date_planned')
        scope='Все мои заявки ({})'.format(str(r_list.count())) 
    context = {
        'scope' : scope,
        'r_list': r_list,
    }
    return render(request, 'request/requests_list.html', context)


@login_required
def actual_requests(request):
    managers=settings.POWER_USERS_GROUP
    if request.user.groups.filter(name__contains = managers):
        r_list=Request.objects.filter(Q(status='N') | Q(status='P')).order_by('date_planned')
        scope='Все текущие заявки  ({})'.format(str(r_list.count())) 
    else:
        r_list=Request.objects.filter(author__username=request.user).filter(Q(status='N') | Q(status='P')).order_by('date_planned')
        scope='Мои текущие заявки  ({})'.format(str(r_list.count()))          
    context = {
        'scope' : scope,
        'r_list': r_list,
    }
    return render(request, 'request/requests_list.html', context)


@login_required
def payed_requests(request):
    managers=settings.POWER_USERS_GROUP
    if request.user.groups.filter(name__contains = managers):
        r_list=Request.objects.filter(status='Y').order_by('date_planned')
        scope='Все оплаченные заявки ({})'.format(str(r_list.count()))        
    else:
        r_list=Request.objects.filter(author__username=request.user).filter(status='Y').order_by('date_planned')
        scope='Мои оплаченные заявки ({})'.format(str(r_list.count()))
    context = {
        'scope' : scope,
        'r_list' : r_list,
    }
    return render(request, 'request/requests_list.html', context)



@login_required
def overdue_requests(request):
    managers=settings.POWER_USERS_GROUP
    if request.user.groups.filter(name__contains = managers):
        r_list=Request.objects.filter(date_planned__lt=timezone.now()-timedelta(days=1)).filter(status='N').order_by('date_planned')
        scope='Все просроченные заявки ({})'.format(str(r_list.count()))
    else:
        r_list=Request.objects.filter(author__username=request.user).filter(date_planned__lt=timezone.now()-timedelta(days=1)).filter(status='N').order_by('date_planned')
        scope='Мои просроченные заявки ({})'.format(str(r_list.count()))        
    context = {
        'scope' : scope,
        'r_list' : r_list,
    }
    return render(request, 'request/requests_list.html', context)