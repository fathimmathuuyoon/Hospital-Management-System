from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ForeignKey


# Create your models here.

class Login(AbstractUser):
    is_doctor = models.BooleanField(default= False)
    is_patient = models.BooleanField(default= False)

class Doctor(models.Model):
    user = models.OneToOneField(Login,on_delete=models.CASCADE,related_name='doctor')
    dept = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10)
    fee = models.IntegerField()

class Patient(models.Model):
    user = models.OneToOneField(Login,on_delete=models.CASCADE,related_name='patients')
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    address = models.TextField()

class Department(models.Model):
    doctor_dept = models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='doc_dep')

class Booking(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    doc_fee = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)


class MedicalReport(models.Model):
    booking = models.ForeignKey(Booking,on_delete=models.CASCADE,related_name='medical_report')
    symptoms = models.TextField()
    diagnosis = models.TextField()
    medicine = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Prescription(models.Model):
    booking = models.ForeignKey(Booking,on_delete=models.CASCADE,related_name='prescriptions')
    medicine_name = models.CharField(max_length=100)
    dose = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    instruction = models.TextField()
    date = models.DateField(auto_now_add=True)

class Bill(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')],
        default='Unpaid'
    )

