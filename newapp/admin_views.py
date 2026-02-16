from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from newapp.filter import DoctorFilter, PatientFilter
from newapp.forms import DoctorRegister
from newapp.models import Doctor, Patient, Department, Bill, Booking


@login_required(login_url='login_view')
def admin_base(request):
    return render(request,'admin/admin_base.html')

@login_required(login_url='login_view')
def view_doctor(request):
    data = Doctor.objects.all()
    doctorFilter = DoctorFilter(request.GET, queryset=data)
    data = doctorFilter.qs
    context = {
        'data': data,
        'doctorFilter': doctorFilter
    }
    return render(request, 'admin/view_doctor.html',context)

@login_required(login_url='login_view')
def edit_doctor(request,id):
    data = Doctor.objects.get(id=id)
    form = DoctorRegister(instance=data)
    if request.method == 'POST':
        form = DoctorRegister(request.POST, instance=data)
        if form.is_valid():
            form.save()
            Department.objects.get_or_create(
                doctor_dept=data,
            )
            return redirect('view_doctor')
    return render(request,'admin/edit_doctor.html',{'form':form})


@login_required(login_url='login_view')
def delete_doctor(request,id):
    data = Doctor.objects.get(id=id)
    data.delete()
    return redirect('view_doctor')


@login_required(login_url='login_view')
def view_patient(request):
    data = Booking.objects.all()
    patientFilter = PatientFilter(request.GET, queryset=data)
    data = patientFilter.qs
    context = {
        'data': data,
        'patientFilter': patientFilter
    }
    return render(request, 'admin/view_patient.html',context)


@login_required(login_url='login_view')
def view_departments(request):
    departments = Doctor.objects.all()
    departmentFilter = PatientFilter(request.GET, queryset=departments)
    departments = departmentFilter.qs
    context = {
        'departments': departments,
        'departmentFilter': departmentFilter
    }
    return render(request, 'admin/view_department.html', context)

@login_required(login_url='login_view')
def view_payment(request):
    billings = Bill.objects.all()
    return render(request, 'admin/view_payment.html', {'billings': billings})

