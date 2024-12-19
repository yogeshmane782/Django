from django import forms
class StudentForm(forms.Form):
    rollno=forms.IntegerField(label="StudentRollno")
    name=forms.CharField(label="StudentName",max_length=20)
    course=forms.CharField(label="StudentCourse", max_length=20)
    fee=forms.IntegerField(label="StudentFee")