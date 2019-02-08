import django_tables2 as tables
from .models import Request
from django_tables2.utils import A

class RequestsList(tables.Table):
    purpose_link = tables.TemplateColumn("<a href='{% url 'this_request' record.id %}'>{{record.purpose}}</a>", verbose_name='Назначение платежа')
    class Meta:
        model = Request
        exclude = ['id', 'date_created', 'purpose']
        sequence = ('date_planned','purpose_link','amount','customer','author','status','costcenter','has_attachments')
        template_name = 'django_tables2/bootstrap4.html'