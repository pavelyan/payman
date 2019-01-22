from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Customer(models.Model):
    customer=models.CharField(max_length=200)

    def __str__(self):
        return self.customer


class Request(models.Model):
    PAYED=(
        ('N','NO'),
        ('Y','YES'),
        ('P','PARTLY')
    )
    purpose=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=12,decimal_places=2)
    date=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=1, choices=PAYED, default='N')
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, null=True, default=None, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}  {}  {}  {}'.format(self.date, self.purpose, self.amount, self.status)
    
