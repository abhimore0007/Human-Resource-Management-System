from django import forms
from .models import Role  

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role 
        fields = ['role_name', 'description']  


        widgets = {
            'role_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter role name (e.g., Admin, Manager)',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a brief description of the role',
                'rows': 4,
            }),
        }

  
        labels = {
            'role_name': 'Role Name',
            'description': 'Role Description',
        }
