from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from newapp.forms import MedicalReportForm
from newapp.models import Doctor, Patient, Booking, MedicalReport

@login_required(login_url='login_view')
def doctor_base(request):
    return render(request,'doctor/doctor_base.html')

@login_required(login_url='login_view')
def view_bookings(request):
    user_data = request.user
    user_doctor = Doctor.objects.get(user=user_data)
    bookings = Booking.objects.filter(doctor=user_doctor)
    return render(request, 'doctor/view_bookings.html', {'bookings': bookings})


@login_required(login_url='login_view')
def view_patients(request):
    doctor = request.user.doctor
    bookings = Booking.objects.filter(doctor=doctor)
    return render(
        request,
        'doctor/view_patients.html',
        {'bookings': bookings}
    )

@login_required(login_url='login_view')
def medical_report(request, id):
    booking = Booking.objects.get(id=id)
    if request.method == 'POST':
        form = MedicalReportForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.booking = booking
            data.save()
            return redirect('medical_history')
    else:
        form = MedicalReportForm()
    return render(
        request,
        'doctor/medical_report.html',{'form': form, 'booking': booking})


@login_required(login_url='login_view')
def medical_history(request):
    user_data = request.user
    doctor = Doctor.objects.get(user=user_data)
    history = MedicalReport.objects.filter(booking__doctor=doctor)
    return render(request,'doctor/medical_history.html',{'history': history})

