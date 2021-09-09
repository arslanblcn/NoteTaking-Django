from django import forms
from django.forms import fields, widgets
from .models import Task

class updateForm(forms.ModelForm):
    class Meta :
        model = Task
        fields = (
            'taskTitle',
            'taskContent',
            'taskComplete'
        )
        widgets = {
            'taskTitle' : forms.TextInput(attrs={'class':'form-control'}),
            'taskContent' : forms.Textarea(attrs={'class':'form-control'}),
        }
        mixed_load = forms.BooleanField(widget=forms.CheckboxInput(attrs={
                'class' : 'form-check-input',
                'id' : 'switchCheck',
            }))