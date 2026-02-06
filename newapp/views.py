from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from newapp.forms import LoginRegister, DoctorRegister, PatientRegister
from newapp.models import Doctor


# Create your views here.

def index(request):
    return render(request,'index.html')

def dashboard(request):
    return render(request,'dashboard.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username = username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('index')
            if user.is_doctor:
                return redirect('index')
            if user.is_patient:
                return redirect('index')
        else:
            print('Invalid credentials')
    return render(request,'loginpage.html')

def doctor_register(request):
    form1 = LoginRegister()
    form2 = DoctorRegister()
    if request.method == 'POST':
        form3 = LoginRegister(request.POST)
        form4 = DoctorRegister(request.POST)
        if form3.is_valid() and form4.is_valid():
            data1 = form3.save(commit=False)
            data1.is_doctor = True
            data1.save()
            data2 = form4.save(commit=False)
            data2.user = data1
            data2.save()
            return redirect('login_view')
    return render(request,'doctor/doctor_register.html',{'form1':form1,'form2':form2})

def patient_register(request):
    form1 = LoginRegister()
    form2 = PatientRegister()
    if request.method == 'POST':
        form3 = LoginRegister(request.POST)
        form4 = PatientRegister(request.POST)
        print('1')
        if form3.is_valid() and form4.is_valid():
            print('11')
            data1 = form3.save(commit=False)
            data1.is_patient = True
            data1.save()
            print(2)
            data2 = form4.save(commit=False)
            data2.user = data1
            data2.save()
            print('3')
            return redirect('login_view')
    return render(request,'patient/patient_register.html',{'form1':form1,'form2':form2})

def user_logout(request):
    logout(request)
    return redirect('login_view')


