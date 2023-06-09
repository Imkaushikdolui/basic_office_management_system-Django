from django.shortcuts import render,HttpResponse
from .models import *
# from datetime import datetime
from emp_app.forms import EmployeeForm,FilterForm

# Create your views here.
def index(request):
    return render(request,'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request,'all_emp.html',context)


def add_emp(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'add_success.html')
        else:
            return HttpResponse('An error occured during Adding new employee')
    context={'form': form}
    return render(request,'add_emp.html',context)


def remove_emp(request,emp_id=None):
    if emp_id:
        emp = Employee.objects.get(id=emp_id)
        emp.delete()
        return render(request,'remove_success.html')
    
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request,'remove_emp.html',context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['first_name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(first_name__icontains=name)
        if dept:
            emps = emps.filter(dept=dept)
        if role:
            emps = emps.filter(role=role)
        context = {
            'emps':emps
        }
        return render(request, 'all_emp.html', context)
    form = FilterForm()
    context = {
        'form':form
    }
    return render(request,'filter_emp.html',context)