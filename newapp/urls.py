from django.urls import path

from newapp import views, admin_views, patient_views, doctor_views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('login_view', views.login_view, name = 'login_view'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('doctor_register', views.doctor_register, name = 'doctor_register'),
    path('patient_register', views.patient_register, name= 'patient_register'),
    path('user_logout', views.user_logout, name='user_logout'),

    path('admin_base', admin_views.admin_base, name='admin_base'),
    path('view_doctor', admin_views.view_doctor, name = 'view_doctor'),
    path('edit_doctor/<int:id>', admin_views.edit_doctor, name = 'edit_doctor'),
    path('delete_doctor/<int:id>', admin_views.delete_doctor, name = 'delete_doctor'),
    path('view_patient', admin_views.view_patient, name='view_patient'),
    path('view_departments', admin_views.view_departments, name='view_departments'),
    path('view_payment', admin_views.view_payment, name='view_payment'),


    path('doctor_base', doctor_views.doctor_base, name='doctor_base'),
    path('view_bookings', doctor_views.view_bookings, name='view_bookings'),
    path('view_patients', doctor_views.view_patients, name='view_patients'),
    path('medical_history/<int:id>', doctor_views.medical_history, name='medical_history'),
    path('medical_report/<int:id>',doctor_views.medical_report,name='medical_report'),
    path('prescription/<int:id>', doctor_views.prescription, name='prescription'),
    # path('view_prescription', doctor_views.view_prescription, name='view_prescription'),

    path('patient_base', patient_views.patient_base, name='patient_base'),
    path('book_doctor', patient_views.book_doctor, name='book_doctor'),
    path('view_report', patient_views.view_report, name='view_report'),
    path('view_prescriptions', patient_views.view_prescriptions, name='view_prescriptions'),
    path('view_bill', patient_views.view_bill, name='view_bill'),
    path('payment/<int:id>', patient_views.payment, name='payment'),

]