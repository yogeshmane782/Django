from django import forms

class UserForm(forms.Form):
    name=forms.CharField(validators="name")
    uname=forms.CharField(validators="username")
    password=forms.IntegerField(validators="password",widget=forms.PasswordInput)
    repassword=forms.IntegerField(validators="repassword",widget=forms.PasswordInput)
    email=forms.CharField(validators="email")