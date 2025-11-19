

from django import forms
class AdditionForm(forms.Form):
    num1 = forms.IntegerField()

    num2 = forms.IntegerField()

class FactorialForm(forms.Form):
    num = forms.IntegerField()

class BmiForm(forms.Form):
    weight= forms.IntegerField()
    height= forms.IntegerField()

class SignupForm(forms.Form):
    username= forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField()
    phone=forms.IntegerField()
    address=forms.CharField(widget=forms.Textarea)

    gender_choice=(('Male','Male'),('Female','Female'))
    gender=forms.ChoiceField(choices=gender_choice,widget=forms.RadioSelect)

    role_choice=(('Admin','Admin'),('student','Student'))
    role=forms.ChoiceField(choices=role_choice)