from django import forms
from .models import *

class TasksForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': "Write a title"}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3',
                                                 'placeholder': "Write a description"}),  
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'important'}),
        }
        labels = {
            'important': 'Mark Important',  
        }


