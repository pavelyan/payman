from django.shortcuts import render, redirect


def start_dispatch(request):
    if request.user.is_authenticated:
        return render(request, 'start.html')
    else:
        return redirect('login')