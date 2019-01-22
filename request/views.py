from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

@login_required
def requests_list(request):
    context = {
        'all_requests': Request.objects.all(),
        'my_requests' : Request.objects.filter(author__username=request.user)
    }
    return render(request, 'request/requests_list.html', context)