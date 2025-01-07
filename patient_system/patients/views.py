from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient

# Create
def create_patient(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        # Create and save the patient
        Patient.objects.create(username=username, password=password, email=email)
        return redirect('read_patients')
    return render(request, 'patients/create_patient.html')

# Read
def read_patients(request):
    patients = Patient.objects.all()
    return render(request, 'patients/read_patients.html', {'patients': patients})

# Update
def update_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        patient.username = request.POST['username']
        patient.email = request.POST['email']
        patient.save()
        return redirect('read_patients')
    return render(request, 'patients/update_patient.html', {'patient': patient})

# Delete
def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        patient.delete()
        return redirect('read_patients')
    return render(request, 'patients/delete_patient.html', {'patient': patient})
