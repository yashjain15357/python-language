from django.db import models

# Create your models here.
# creating company model

com_type = (("IT" , "IT"),("Non It","NON IT"),("mobile" ,"Mobile company"))
class Company(models.Model):
    comp_ID = models.CharField(max_length=50, unique=True , primary_key=True )
    comp_name = models.CharField(max_length=100)
    comp_address = models.CharField(max_length=100)
    comp_about = models.TextField()
    comp_type = models.CharField(max_length=100,choices=com_type)
    comp_data = models.DateTimeField(auto_now=True)
    comp_active = models.BooleanField(default=True)

    def __str__(self):
        return self.comp_name

# Employee model

class Employee(models.Model):
    emp_ID = models.CharField(max_length=10, primary_key=True)
    emp_name = models.CharField(max_length=50, null=False)
    emp_address = models.CharField(max_length=100)
    emp_number = models.CharField(max_length=10)
    emp_positon = models.CharField(max_length=50)
    comp_ID = models.ForeignKey(Company,on_delete=models.CASCADE)