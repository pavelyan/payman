from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)

class RequestAdmin(admin.ModelAdmin):
    list_display=[
        'date_planned',
        'purpose',
        'amount',
        'customer',
        'author',
        'status',
        'costcenter'
    ]
    ordering=['-date_planned']

admin.site.register(Request, RequestAdmin)

admin.site.register(CostCenter)