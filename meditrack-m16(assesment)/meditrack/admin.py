# core/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, DoctorProfile, Appointment, MedicalRecord

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Role & Avatar', {'fields': ('role', 'avatar')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')


@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'scheduled_time', 'status')
    list_filter = ('status', 'doctor')
    search_fields = ('patient__username', 'doctor__username')


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'patient', 'uploaded_by', 'uploaded_at')
    search_fields = ('title', 'patient__username')
