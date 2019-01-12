from django.contrib import admin

from queries.models import Query,Customers


@admin.register(Query)
class AdminQueries(admin.ModelAdmin):
    list_display=['customer','purpose','amount_plan','date_plan','pay_status']


@admin.register(Customers)
class AdminCustomers(admin.ModelAdmin):
    pass