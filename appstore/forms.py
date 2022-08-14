from django import forms
from django.forms import ModelForm
from .models import Customers



class Customers(ModelForm):
    class Meta:
        model = Customers
        fields = ('Gender_choic','firstName','lastName','Gender',' Age','Profile','RegistrationDate')
        labels = {
            'Gender_choic': '',
            'firstName': '',
            'lastName': '',
            'Gender': '',
            'Age': '',
            'Profile': '',
            'RegistrationDate': '',

        }

        widgets = {
            'Gender_choic': forms.TextInput(attrs={'class':'form-control', 'plceholder':'Gender_choic'}),
            'firstName': forms.TextInput(attrs={'class':'form-control','plceholder':'firstName'}),
            'lastName': forms.TextInput(attrs={'class':'form-control','plceholder':'lastName'}),
            'Gender': forms.TextInput(attrs={'class':'form-control','plceholder':'Gender'}),
            'Age': forms.TextInput(attrs={'class':'form-control','plceholder':'Age'}),
            'Profile': forms.TextInput(attrs={'class':'form-control','plceholder':'Profile'}),
            'RegistrationDate': forms.TextInput(attrs={'class':'form-control','plceholder':'RegistrationDate'}),

        }




       