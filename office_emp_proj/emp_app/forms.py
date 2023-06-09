from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    
    class Meta:
        model = Employee
        fields = '__all__'

class FilterForm(ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ('last_name','salary', 'bonus','phone','hire_date')