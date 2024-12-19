from django.core.exceptions import ValidationError
def name_validator(value):
    if not value.isupper():
        raise ValidationError("Name must be in uppercase")
def uname_validator(value):
    if not value.isalnum():
        raise ValidationError("uname must be alpha numeric")
def pwd_validator(value):
    ac,dc,sc=0,0,0
    for ch in value:
        if ch.isalpha():
            ac+=1
        elif ch.isdigit():
            dc+=1
        else:
            sc+=1
    if ac>=4 and dc>=2 and sc>=2:
        pass
    else:
        raise ValidationError("Invalid password")
    