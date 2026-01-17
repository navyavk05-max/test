from django.shortcuts import render
from rest_framework import status
from rest_framework . response import Response
from rest_framework . views import APIView
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.
# CREATE & READ by ID
class EmployeeDetail(APIView):
    
    # FETCH EMPLOYEE BYID
    def get(self, request,pk):
        try:
            Employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(
                {"error": "employee not found"},
                ststus=status.HTTP_404_NOT_FOUND
            )
        
        serializer = EmployeeSerializer(Employee)
        return Response(serializer.data)  

    # UPDATE EMPLOYEE  
    def put(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(
                {"error": "employee not found"},
                status=status.HTTP_404_NOT_FOUND
            )    
        
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
#    DELETE
    def delete(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(
                {"error": "Employee not found"},
                status=status.HTTP_404_NOT_FOUND
            )    
        
        employee.status = "Inactive"
        employee.save()
        return Response(
            {"message": "employee marked as Inactive"},
            status=status.HTTP_200_OK
        )
    
# ADD EMPLOYEE  
class EmployeeCreate(APIView):
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(status="Active")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
    
