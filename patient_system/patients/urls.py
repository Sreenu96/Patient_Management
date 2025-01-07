from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_patient, name='create_patient'),
    path('read/', views.read_patients, name='read_patients'),
    path('update/<int:patient_id>/', views.update_patient, name='update_patient'),
    path('delete/<int:patient_id>/', views.delete_patient, name='delete_patient'),
]

