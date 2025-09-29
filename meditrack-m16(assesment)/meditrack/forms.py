# core/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Appointment, MedicalRecord

class PatientSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'role', 'avatar')
        # Set role default in the view to 'patient' or hide it

class DoctorSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'role', 'avatar')

class AppointmentForm(forms.ModelForm):
    scheduled_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    class Meta:
        model = Appointment
        fields = ['doctor', 'scheduled_time', 'reason']

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['title', 'description', 'file']
