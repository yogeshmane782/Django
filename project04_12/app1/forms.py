from django import forms

class PersonForm(forms.Form):
    name=forms.CharField(label="name", max_length=20)
    age=forms.IntegerField(label="age")
    city=forms.CharField(label="city" ,max_length=20)

    def clean_name(self):
        name=self.cleaned_data['name']
        if len(name)>20:
            raise forms.ValidationError("Name must be less than 20 characters")
        else:
            return name
    def clean_age(self):
        age=self.cleaned_data['age']
        if age>18 and age<70:
            return age
        else:
            raise forms.ValidationError("age must be >18 and <70")
    def clean_city(self):
        city=self.cleaned_data['city']
        if city in ["hyd","pune"]:
            return city
        else:
            raise forms.ValidationError("city must be hyd ir pune")

        