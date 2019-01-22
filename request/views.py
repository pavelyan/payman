from django.shortcuts import render
from .models import *

# Create your views here.

def requests_list(request):
    context = {
        'all_requests': Request.objects.all(),
        'my_requests' : Request.objects.filter(author__username=request.user)
    }
    return render(request, 'request/requests_list.html', context)