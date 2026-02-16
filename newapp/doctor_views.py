from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from newapp.filter import PatientFilter, BookingFilter
from newapp.forms import MedicalReportForm, PrescriptionForm
from newapp.models import Doctor, Booking, MedicalReport, Prescription


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
    user_data = request.user
    user_doctor = Doctor.objects.get(user=user_data)
    bookings = Booking.objects.filter(doctor=user_doctor)
    bookingFilter = BookingFilter(request.GET, queryset=bookings)
    bookings = bookingFilter.qs
    context = {
        'bookings': bookings,
        'bookingFilter': bookingFilter
    }
    return render(request,'doctor/view_patients.html',context)

@login_required(login_url='login_view')
def medical_report(request, id):
    booking = Booking.objects.get(id=id)
    if request.method == 'POST':
        form = MedicalReportForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.booking = booking
            data.save()
            return redirect('medical_history',id=booking.id)
    else:
        form = MedicalReportForm()
    return render(
        request,
        'doctor/medical_report.html',{'form': form, 'booking': booking})


@login_required(login_url='login_view')
def medical_history(request,id):
    user_data = request.user
    user_doctor = Doctor.objects.get(user=user_data)
    history = MedicalReport.objects.filter(booking_id=id,booking__doctor=user_doctor)
    return render(request,'doctor/medical_history.html', {'history': history})


@login_required(login_url='login_view')
def prescription(request, id):
    booking = Booking.objects.get(id=id)
    if request.method == "POST":
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.booking = booking
            data.doctor = request.user.doctor
            data.save()
            return redirect('view_patients')
    else:
        form = PrescriptionForm()

    return render(request, 'doctor/prescription.html', {'form': form, 'booking':booking})

# @login_required(login_url='login_view')
# def view_prescription(request):
#     doctor = request.user.doctor
#     prescription = Prescription.objects.filter(booking__doctor=doctor)
#     return render(request,'doctor/view_prescription.html',{'prescription': prescription})