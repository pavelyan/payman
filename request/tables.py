import django_tables2 as tables
from .models import Request


class RequestTable(tables.Table):
    purpose = tables.Column(verbose_name='Назначение')
    date_planned = tables.Column(verbose_name='Дата платежа')
    amount = tables.Column(verbose_name='Сумма')
    customer = tables.Column(verbose_name='Контрагент')
    author = tables.Column(verbose_name="Инициатор")
    status = tables.Column(verbose_name='Оплачено')
    costcenter = tables.Column(verbose_name='ЦФО')

    class Meta:
        model = Request
        sequence = ('id','date_planned','purpose','amount','customer','author','status','costcenter')
        template_name = 'django_tables2/bootstrap4.html'