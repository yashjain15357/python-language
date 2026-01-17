# The interface you are seeing is called the Browsable API. It is a built-in feature of the Django REST Framework (DRF) that provides a user-friendly HTML representation of your API when you access it via a web browser.


from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Company , Employee
from .serailizer import companySerializer , employeeSerializer

from rest_framework.decorators import action
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet): 
    queryset =Company.objects.all()
    serializer_class = companySerializer

    # custom url for fech all the employee of particular company
    
    @action(detail=True, methods=['get', 'post', 'put'])
    def employee(self , request , pk=None):
        company = Company.objects.get(pk=pk)
        employee = Employee.objects.filter(comp_ID = company)

        emp_serializer = employeeSerializer(employee , many = True , context ={'request':request})
        return  Response(emp_serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer
    
#  A viewset that provides default `create()`, `retrieve()`, `update()`, `partial_update()`, `destroy()` and `list()` actions.