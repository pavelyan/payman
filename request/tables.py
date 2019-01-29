import django_tables2 as tables
from .models import Request


class RequestsList(tables.Table):

    class Meta:
        model = Request
        sequence = ('id','date_planned','purpose','amount','customer','author','status','costcenter')
        template_name = 'django_tables2/bootstrap4.html'