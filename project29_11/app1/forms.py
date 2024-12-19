from django import forms
class RegisterForms(forms.Form):
    name=forms.CharField(label="Name", max_length=20)
    user=forms.CharField(label="UserName",max_length=20)
    pwd=forms.CharField(label="Password",widget=forms.PasswordInput)
