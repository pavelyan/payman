from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Customers(models.Model):
    cust_name=models.CharField(max_length=200)

    def __str__(self):
        return self.cust_name


class Query(models.Model):
    PAYED=[(0,'No'),(1,'Completely'),(2,'Partially')]
    purpose=models.CharField(max_length=100)
    amount_plan=models.DecimalField(max_digits=12,decimal_places=2)
    date_plan=models.DateTimeField(default=timezone.now)
    pay_status=models.PositiveSmallIntegerField(choices=PAYED, default=0)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customers, null=True, default=None, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{} : {} : {}'.format(self.purpose, self.amount_plan, self.pay_status)
