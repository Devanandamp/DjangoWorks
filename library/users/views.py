from django.shortcuts import render,redirect
from django.views import View



# def register(request):
#     return render(request,'register.html')
# def login(request):
#     return render(request,'login.html')

from django.views import View
from .forms import SignupForm
class Register(View):
    def post(self, request):
        form_instance =SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('users:userlogin')
        context = {'form':form_instance}
        return render(request, 'register.html', context)

    def get(self, request):
        form_instance=SignupForm()
        context = {'form':form_instance}
        return render(request, 'register.html', context)

from .forms import  LoginForm
from django.contrib import  messages
from django.contrib.auth import authenticate, login, logout
class Userlogin(View):
    def post(self, request):
        form_instance =LoginForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data #fetch the data after validation
            u=data['username']   #retrieve username from cleaned_data
            p=data['password']   #         password
            user=authenticate(username=u,password=p)  #calls authenticate() to verify if user exist
                                                      #if record exists then it returns user object as response
                                                      #else none
            if user: #if user exists
                login(request,user)  #adds the user into current session
                return redirect('books:home')
            else:  #if user does not exist
                messages.error(request, "invalid credentials")
                return redirect('users:userlogin')

    def get(self, request):
        form_instance =LoginForm()
        context = {'form':form_instance}
        return render(request, 'login.html', context)

class Userlogout(View):
    def get(self, request):
        logout(request)  #removes the user from the current session
        return redirect ('users:userlogin')

