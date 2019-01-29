from django.shortcuts import render
from .models import *
from django_tables2 import RequestConfig
from .tables import RequestsList
from django.db.models import Sum


def requests_table(request, qs_tmp, t_header):
    """ if used in view, wrappes passed queryset to django-tables custom class RequestTable
        args: 1) request 2) ORM queryset 3) topic header 4) template to render all stuff into """
    s = qs_tmp.aggregate(Sum('amount'))['amount__sum']
    if s==None:
        s=0        
    scope='Соответствующих заявок: {} (на сумму {:,} руб.)'.format(str(qs_tmp.count()),s).replace(',', ' ')
    r_list=RequestsList(qs_tmp)
    RequestConfig(request,paginate={'per_page': 20}).configure(r_list)
    topic_header = t_header
    context = {
        'topic_header' : topic_header,
        'scope' : scope,
        'r_list': r_list,
    }
    return render(request, 'request/requests_list.html', context)
