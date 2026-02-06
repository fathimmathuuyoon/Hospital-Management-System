from django.contrib.auth.forms import UserCreationForm
from django import forms

from newapp.models import Login, Doctor, Patient, MedicalReport


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget= forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username','password1','password2')

class DoctorRegister(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = '__all__'
        exclude = ('user',)


class PatientRegister(forms.ModelForm):

    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ('user',)


class MedicalReportForm(forms.ModelForm):
    class Meta:
        model = MedicalReport
        fields = ['symptoms', 'diagnosis', 'prescription',]