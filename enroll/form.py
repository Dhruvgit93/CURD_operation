from django import forms
from .models import student

class register(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }

    def clean_name(self):
        valname=self.cleaned_data['name']
        if not str(valname.replace(' ','')).isalpha():
            raise forms.ValidationError('Field Should not contain any speacial character or Number')
        return valname
    def clean_email(self):
        valemail=self.cleaned_data['email']
        if '@gmail.com' not in valemail:
            raise forms.ValidationError('Only Gmail account is acceptable')
        return valemail
    