from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.conf import settings
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import Q
from django_tables2 import RequestConfig
from django.db.models import Sum
from .models import *
from .tables import RequestsList
from .utils import requests_table
from .forms import *

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
        qset = Request.objects.filter(date_planned__lt=timezone.now()-timedelta(days=1)).exclude(status='Y').order_by('date_planned')
    else:
        qset=Request.objects.filter(author__username=request.user).filter(date_planned__lt=timezone.now()-timedelta(days=1)).exclude(status='Y').order_by('date_planned')
    return requests_table(request, qset, 'Просроченные заявки')


@login_required
def new_request(request):
    if request.method == 'POST':
        new_request_form = NewRequestForm(request.POST)
        file_upload_form = UploadForm(request.POST, request.FILES)
        files = request.FILES.getlist('scan')
        if new_request_form.is_valid() and file_upload_form.is_valid():

            new_request = new_request_form.save(commit=False)
            new_request.author = request.user
            if bool(request.FILES.get('scan', False)) == True:
                new_request.has_attachments=True
            else:
                new_request.has_attachments=False
            new_request.save()
            # adding m2m records
            if files != None:
                for f in files:
                    uploads = Upload(scan=f, user=request.user)
                    uploads.save()
                    new_request.documents.add(uploads.id)
                                   
            return redirect('all_requests')
    else:
        new_request_form = NewRequestForm()
        file_upload_form = UploadForm()
    context ={
        'new_request_form' : new_request_form,
        'file_upload_form' : file_upload_form
    }
    return render(request, 'request/new_request_form.html', context)


class RequestDetailView(DetailView):
    model = Request
    template_name = 'request/this_request.html'


@login_required
def request_details(request, pk):
    qs = Request.objects.filter(id=pk).get()
    a = qs.documents.select_related().values_list('scan', flat=True)
    attachments = []
    for i in a:
        attachments.append(i)
    url = request.scheme+"://"+request.get_host()+settings.MEDIA_URL
    context = {
        'id' : qs.id,
        'purpose' : qs.purpose,
        'date_created' : qs.date_created,
        'date_planned' : qs.date_planned,
        'author' : qs.author,
        'amount' : qs.amount,
        'customer' : qs.customer,
        'costcenter' : qs.costcenter,
        'attachments' : attachments,
        'url' : url,
    }
    return render(request, 'request/this_request.html', context)