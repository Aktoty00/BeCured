from django.urls import path, re_path
from . import views
urlpatterns = [
    # path('', views.main),
    path('login/', views.login),
    # path('signup/', views.signup),
    path('doctor_lists/', views.DoctorList.as_view()),
    path('doctor_lists/<int:pk>/', views.DoctorDetail.as_view()),
    # path('patient_page', views.patientPage),
    path('treatment_lists/', views.TreatmentLists),
    path('treatment_lists/<int:pk>/', views.TreatmentListsDetail),
    # path('request_page', views.requestPage),
    # path('doctor_page', views.doctorPage),
    path('patient_lists/', views.PatientList.as_view()),
    path('patient_lists/<int:pk>/', views.PatientDetail.as_view()),
    # path('add_patient', views.addPatient),
    path('appointment_lists/', views.AppointmentLists.as_view()),
    path('appointment_lists/<int:pk>/', views.AppointmentListDetail.as_view()),
    # path('response_page', views. responsePage),
    # path('request_lists/<int:pk>/', views.requestListDetail.as_view()),
    # path('response_page', views.responsePage),
    path('logout/', views.logout),
    path('users/', views.UserList.as_view()),
]
