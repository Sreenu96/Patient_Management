# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Patient

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = make_password(request.POST['password'])

        # Save to database
        Patient.objects.create(username=username, password=password)
        return redirect('login')

    return render(request, 'patients/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check user in the database
        try:
            patient = Patient.objects.get(username=username)
            if check_password(password, patient.password):
                return render(request, 'patients/welcome.html', {'patient': patient})
            else:
                return render(request, 'patients/login.html', {'error': 'Invalid password'})
        except Patient.DoesNotExist:
            return render(request, 'patients/login.html', {'error': 'User does not exist'})

    return render(request, 'patients/login.html')
