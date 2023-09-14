from django import forms

from .models import CustRegst

class CustRegstForm(forms.ModelForm):
    class Meta:
        model = CustRegst
        fields = '__all__'
        widgets = {
            'password' : forms.PasswordInput(),
            'date_of_birth' : forms.SelectDateWidget(),
        }