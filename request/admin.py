from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)

class RequestAdmin(admin.ModelAdmin):
    list_display=[
        'date',
        'purpose',
        'amount',
        'customer',
        'author',
        'status'
    ]
    ordering=['-date']

admin.site.register(Request, RequestAdmin)