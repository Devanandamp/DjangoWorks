from webbrowser import register

from django.contrib import admin
from app1.models import Student_model

from library.books.models import Book
from studentapp.app1.models import Student_model

admin.site.register(Student_model)
