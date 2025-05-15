from django.contrib.auth.models import User 
from django.forms import ModelForm

class SignUp(ModelForm):

    class Meta:
        model:User
        field=["f_name","l_name","username","password"]