from django.db import models

# Create your models here.

class Departments(models.Model):
    DepartmentID=models.AutoField(primary_key=True)
    DepartmentID=models.CharField(max_length=100)

class Employees(models.Model):
    EmployeesId = models.AutoField(primary_key=True)
    EmployeeId=models.CharField(max_length=100)
    Departments = models.CharField(max_length=100)
    DataofJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=100) 

