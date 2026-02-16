import django_filters
from django import forms
from django_filters import CharFilter

from newapp.models import Doctor, Patient, Department, Booking


class DoctorFilter(django_filters.FilterSet):
    name = CharFilter(label='', lookup_expr='icontains',
        widget=forms.TextInput(
        attrs={'placeholder': 'Search doctor',
               'class':'form-control'}))
    class Meta:
        model:Doctor
        fields= ('name',)

class PatientFilter(django_filters.FilterSet):
    name = CharFilter(label='', lookup_expr='icontains',
        widget=forms.TextInput(
        attrs={'placeholder': 'Search patient',
               'class':'form-control'}))
    class Meta:
        model:Patient
        fields= ('name',)

class DepartmentFilter(django_filters.FilterSet):
    doctor_dept__dept = CharFilter(label='', lookup_expr='icontains',
        widget=forms.TextInput(
        attrs={'placeholder': 'Search department',
               'class':'form-control'}))
    class Meta:
        model:Department
        fields= ('doctor_dept__dept',)

class BookingFilter(django_filters.FilterSet):
    patient__name = CharFilter(label='', lookup_expr='icontains',
        widget=forms.TextInput(
        attrs={'placeholder': 'Search patient',
               'class':'form-control'}))
    class Meta:
        model:Booking
        fields= ('patient__name',)


