from django import forms  
from employee.models import Employee  

# create emplloyee form
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"
