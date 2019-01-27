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

# Create your views here.


@login_required
def all_requests(request):
    managers=settings.POWER_USERS_GROUP
    if request.user.groups.filter(name__contains = managers):
        tmp = Request.objects.all()
        s=tmp.aggregate(Sum('amount'))['amount__sum']
        if s==None:
            s=0        
        scope='Всего заявок {}, на сумму {:,} руб.'.format(str(tmp.count()),s).replace(',', ' ')
        r_list=RequestTable(tmp)
        RequestConfig(request,paginate={'per_page': 20}).configure(r_list)
    else:
        tmp=Request.objects.filter(author__username=request.user).order_by('date_planned')
        s=tmp.aggregate(Sum('amount'))['amount__sum']
        if s==None:
            s=0        
        scope='Всего заявок {}, на сумму {:,} руб.'.format(str(tmp.count()),s).replace(',', ' ') 
        r_list=RequestTable(tmp)
        RequestConfig(request,paginate={'per_page': 20}).configure(r_list)
    context = {
        'scope' : scope,
        'r_list': r_list,
    }
    return render(request, 'request/requests_list.html', context)


@login_required
def actual_requests(request):
    managers=settings.POWER_USERS_GROUP
    if request.user.groups.filter(name__contains = managers):
        tmp=Request.objects.filter(Q(status='N') | Q(status='P')).order_by('date_planned')
        s=tmp.aggregate(Sum('amount'))['amount__sum']
        if s==None:
            s=0        
        scope='Открытых заявок {}, на сумму {:,} руб.'.format(str(tmp.count()),s).replace(',', ' ')
        r_list=RequestTable(tmp)
        RequestConfig(request,paginate={'per_page': 20}).configure(r_list)
    else:
        tmp=Request.objects.filter(author__username=request.user).filter(Q(status='N') | Q(status='P')).order_by('date_planned')
        s=tmp.aggregate(Sum('amount'))['amount__sum']
        if s==None:
            s=0        
        scope='Открытых заявок {}, на сумму {:,} руб.'.format(str(tmp.count()),s).replace(',', ' ')
        r_list=RequestTable(tmp)
        RequestConfig(request,paginate={'per_page': 20}).configure(r_list)                 
    context = {
        'scope' : scope,
        'r_list': r_list,
    }
    return render(request, 'request/requests_list.html', context)


@login_required
def payed_requests(request):
    managers=settings.POWER_USERS_GROUP
    if request.user.groups.filter(name__contains = managers):
        tmp=Request.objects.filter(status='Y').order_by('date_planned')
        s=tmp.aggregate(Sum('amount'))['amount__sum']
        if s==None:
            s=0        
        scope='Оплаченных заявок {}, на сумму {:,} руб.'.format(str(tmp.count()),s).replace(',', ' ')   
        r_list=RequestTable(tmp)
        RequestConfig(request,paginate={'per_page': 20}).configure(r_list)               
    else:
        tmp=Request.objects.filter(author__username=request.user).filter(status='Y').order_by('date_planned')
        s=tmp.aggregate(Sum('amount'))['amount__sum']
        if s==None:
            s=0        
        scope='Оплаченных заявок {}, на сумму {:,} руб.'.format(str(tmp.count()),s).replace(',', ' ')   
        r_list=RequestTable(tmp)
        RequestConfig(request,paginate={'per_page': 20}).configure(r_list)           
    context = {
        'scope' : scope,
        'r_list' : r_list,
    }
    return render(request, 'request/requests_list.html', context)


@login_required
def overdue_requests(request):
    managers=settings.POWER_USERS_GROUP
    if request.user.groups.filter(name__contains = managers):
        tmp=Request.objects.filter(date_planned__lt=timezone.now()-timedelta(days=1)).filter(status='N').order_by('date_planned')
        s=tmp.aggregate(Sum('amount'))['amount__sum']
        if s==None:
            s=0        
        scope='Просроченных заявок {}, на сумму {:,} руб.'.format(str(tmp.count()),s).replace(',', ' ')   
        r_list = RequestTable(tmp)
        RequestConfig(request,paginate={'per_page': 20}).configure(r_list)
    else:
        tmp=Request.objects.filter(author__username=request.user).filter(date_planned__lt=timezone.now()-timedelta(days=1)).filter(status='N').order_by('date_planned')
        s=tmp.aggregate(Sum('amount'))['amount__sum']
        if s==None:
            s=0
        scope='Просроченных заявок {}, на сумму {:,} руб.'.format(str(tmp.count()),s).replace(',', ' ')  
        r_list=RequestTable(tmp)
        RequestConfig(request,paginate={'per_page': 20}).configure(r_list)                  
    context = {
        'scope' : scope,
        'r_list' : r_list,
    }
    return render(request, 'request/requests_list.html', context)