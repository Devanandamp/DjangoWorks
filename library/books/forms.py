from django import forms

from books.models import Book
from django.contrib.auth.models import User



# class Addbookform(forms.Form):
#     title=forms.CharField()
#     author=forms.CharField()
#     price=forms.IntegerField()
#     pages=forms.IntegerField()
#     language=forms.CharField()


class Addbookform(forms.ModelForm):
    class Meta:
        model = Book
        fields="__all__"


