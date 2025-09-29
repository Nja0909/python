# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import PatientSignupForm, DoctorSignupForm, AppointmentForm, MedicalRecordForm
from .models import Appointment, MedicalRecord, User
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

def is_doctor(user):
    return user.is_authenticated and user.role == 'doctor'

def is_patient(user):
    return user.is_authenticated and user.role == 'patient'


def signup_patient(request):
    if request.method == 'POST':
        form = PatientSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'patient'
            user.save()
            login(request, user)
            messages.success(request, "Patient account created.")
            return redirect('core:dashboard')
    else:
        form = PatientSignupForm()
    return render(request, 'core/signup.html', {'form': form})


def signup_doctor(request):
    if request.method == 'POST':
        form = DoctorSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'doctor'
            user.save()
            messages.success(request, "Doctor account created.")
            return redirect('core:doctor_dashboard')
    else:
        form = DoctorSignupForm()
    return render(request, 'core/signup.html', {'form': form})


@login_required
def dashboard(request):
    # patient dashboard
    if request.user.role == 'patient':
        appointments = request.user.appointments_as_patient.all().order_by('-scheduled_time')
        return render(request, 'core/patient_dashboard.html', {'appointments': appointments})
    elif request.user.role == 'doctor':
        return redirect('core:doctor_dashboard')
    else:
        return render(request, 'core/dashboard.html')


@login_required
@user_passes_test(is_patient)
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            # validation: doctor must have role doctor
            if appointment.doctor.role != 'doctor':
                messages.error(request, "Selected user is not a doctor.")
                return redirect('core:book_appointment')

            if appointment.scheduled_time <= timezone.now():
                messages.error(request, "Scheduled time must be in the future.")
                return redirect('core:book_appointment')

            appointment.save()
            messages.success(request, 'Appointment requested. You will be notified on confirmation.')
            # send email to doctor (example)
            try:
                send_mail(
                    'New Appointment Requested',
                    f'Patient {request.user.username} requested an appointment at {appointment.scheduled_time}.',
                    settings.DEFAULT_FROM_EMAIL,
                    [appointment.doctor.email],
                )
            except Exception:
                pass
            return redirect('core:dashboard')
    else:
        form = AppointmentForm()
    return render(request, 'core/book_appointment.html', {'form': form})


@login_required
@user_passes_test(is_doctor)
def doctor_dashboard(request):
    # doctor sees pending appointments to confirm/reschedule
    appointments = request.user.appointments_as_doctor.filter(status__in=['pending', 'rescheduled']).order_by('scheduled_time')
    return render(request, 'core/doctor_dashboard.html', {'appointments': appointments})


@login_required
@user_passes_test(is_doctor)
def update_appointment_status(request, appointment_id):
    appt = get_object_or_404(Appointment, id=appointment_id, doctor=request.user)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'confirm':
            appt.status = 'confirmed'
            appt.save()
            # optionally email patient
            try:
                send_mail(
                    'Appointment Confirmed',
                    f'Your appointment at {appt.scheduled_time} with Dr. {appt.doctor.get_full_name()} is confirmed.',
                    settings.DEFAULT_FROM_EMAIL,
                    [appt.patient.email],
                )
            except Exception:
                pass
            messages.success(request, 'Appointment confirmed.')
        elif action == 'reschedule':
            # reschedule logic: set new time from form
            new_time = request.POST.get('new_time')
            # parse and set - for brevity assume valid
            appt.scheduled_time = new_time
            appt.status = 'rescheduled'
            appt.save()
            messages.success(request, 'Appointment rescheduled.')
        elif action == 'complete':
            appt.status = 'completed'
            appt.save()
            messages.success(request, 'Appointment marked as completed.')
        return redirect('core:doctor_dashboard')

    return render(request, 'core/update_appointment.html', {'appointment': appt})


@login_required
def upload_medical_record(request, appointment_id=None):
    if appointment_id:
        appt = get_object_or_404(Appointment, id=appointment_id)
        # only doctor can upload to this appointment
        if request.user != appt.doctor and not request.user.is_staff:
            messages.error(request, "Not allowed.")
            return redirect('core:dashboard')

    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, request.FILES)
        if form.is_valid():
            mr = form.save(commit=False)
            mr.uploaded_by = request.user
            # who is the patient? if appointment given, get its patient; else pick from form or current user
            if appointment_id:
                mr.patient = appt.patient
                mr.appointment = appt
            else:
                # for admin / doctor uploading not tied to appointment you'd add selection in form
                pass
            mr.save()
            messages.success(request, "Medical record uploaded.")
            return redirect('core:dashboard')
    else:
        form = MedicalRecordForm()
    return render(request, 'core/upload_record.html', {'form': form})
