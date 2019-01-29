from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User


class Customer(models.Model):
    customer=models.CharField(max_length=200)

    def __str__(self):
        return self.customer

class CostCenter(models.Model):
    INN=models.CharField(max_length=12, unique=True)
    abbrev_name=models.CharField(max_length=10)
    fullname=models.CharField(max_length=255)

    def __str__(self):
        return self.abbrev_name


class Request(models.Model):
    PAYED=(
        ('N','Нет'),
        ('Y','Да'),
        ('P','Часть')
    )
    purpose=models.CharField(max_length=100, verbose_name='Назначение платежа')
    amount=models.DecimalField(max_digits=12,decimal_places=2, verbose_name='Требуемая сумма')
    date_planned=models.DateTimeField(default=timezone.now, verbose_name='Планируемая дата')
    status=models.CharField(max_length=1, choices=PAYED, default='N', verbose_name='Оплачено')
    author=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Инициатор')
    customer=models.ForeignKey(Customer, null=True, default=None, blank=True, on_delete=models.CASCADE, verbose_name='Контрагент')
    costcenter=models.ForeignKey(CostCenter, null=True, default=None, blank=True, on_delete=models.CASCADE, verbose_name='ЦФО')

    def __str__(self):
        return '{}  {}  {}  {}'.format(self.date_planned, self.purpose, self.amount, self.status)
    
