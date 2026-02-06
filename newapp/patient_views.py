from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from newapp.models import Doctor, Patient, Booking, MedicalReport

@login_required(login_url='login_view')
def patient_base(request):
    return render(request,'patient/patient_base.html')


@login_required(login_url='login_view')
def book_doctor(request):
    user_data = request.user
    doctors = Doctor.objects.all()
    patient = Patient.objects.get(user=user_data)
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor')
        if doctor_id:
            doctor = Doctor.objects.get(id=doctor_id)
            Booking.objects.create(
                patient=patient,
                doctor=doctor)
            return redirect('patient_base')
    return render(request, 'patient/book_doctor.html', {'doctors': doctors})


@login_required(login_url='login_view')
def view_report(request):
    patient = Patient.objects.get(user=request.user)
    history = MedicalReport.objects.filter(booking__patient=patient)
    return render(request,'patient/view_report.html',{'history': history})