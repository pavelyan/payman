from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<username>/<filename>
    return '{0}/{1}'.format(instance.user.username, filename)


class Upload(models.Model):
    scan=models.FileField(upload_to=user_directory_path, verbose_name='Вложенные документы')
    date_uploaded = models.DateTimeField(default=timezone.now, verbose_name='Дата/время')
    user=models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Кем загружен')


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
    date_planned=models.DateField(default=timezone.now().today, verbose_name='Планируемая дата')
    date_created=models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    status=models.CharField(max_length=1, choices=PAYED, default='N', verbose_name='Оплачено')
    author=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Инициатор')
    customer=models.ForeignKey(Customer, null=True, default=None, blank=True, on_delete=models.CASCADE, verbose_name='Контрагент')
    costcenter=models.ForeignKey(CostCenter, null=True, default=None, blank=True, on_delete=models.CASCADE, verbose_name='ЦФО')
    has_attachments=models.BooleanField(default=False, verbose_name = 'Вложения')
    documents=models.ManyToManyField(Upload, blank=True, verbose_name='Вложенные документы')

    def __str__(self):
        return '{}  {}  {}  {}'.format(self.date_planned, self.purpose, self.amount, self.status)

    def get_absolute_url(self):
        return reverse('this_request', kwargs={'pk':self.pk})
    

