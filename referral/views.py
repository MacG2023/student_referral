from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import AdmissionTransaction

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'referral/login.html', {'error': 'Invalid username or password'})
    return render(request, 'referral/login.html')

@login_required
def home_view(request):
    transactions = AdmissionTransaction.objects.filter(created_by=request.user)
    return render(request, 'referral/home.html', {'transactions': transactions})
