from django.urls import path
from api3 import views



urlpatterns=[
    path('studentapi/',views.student_api,name='Studentapi'),
    
]