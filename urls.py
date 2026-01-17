from django.urls import path
from .views import EmployeeCreate, EmployeeDetail

urlpatterns = [
     path('employees/', EmployeeCreate.as_view()),
     path('employees/<int:pk>/', EmployeeDetail.as_view()),
     
]
