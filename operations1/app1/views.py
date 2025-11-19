from django.shortcuts import render
from django.views import View
from app1.forms import AdditionForm,FactorialForm,BmiForm



#CLASS based
class Addition(View):
    def get(self,request):
        form_instance = AdditionForm()
        context = {'form': form_instance}
        return render(request,'addition.html',context)
    def post(self,request):
        # print(request.POST) #submitted data
        #creating from object using submitted data
        form_instance = AdditionForm(request.POST)
        #check whether data is valid
        if form_instance.is_valid():
        #process data
               data=form_instance.cleaned_data
               #print('cleaned_data',data)
               n1=data['num1']
               n2=data['num2']
               sum=n1+n2
               context={'result':sum,'form':form_instance}
               return render(request,'addition.html',context)

class Factorial(View):
    def get(self, request):
        form_instance = FactorialForm()
        context = {'form': form_instance}
        return render(request, 'fact.html',context)
    def post(self,request):
        #creating from object using submitted data
        form_instance = FactorialForm(request.POST)
        #check whether data is valid
        if form_instance.is_valid():
        #process data
               data=form_instance.cleaned_data
               print('cleaned_data',data)
               n=data['num']
               f=1
               for i in range(1,n+1):
                   f=f*i
               context={'result':f,'form':form_instance}
               return render(request,'fact.html',context)

class BMI(View):
    def get(self, request):
        form_instance = BmiForm()
        context = {'form': form_instance}
        return render(request, 'bmi.html',context)
    def post(self,request):
        #creating from object using submitted data
        form_instance = BmiForm(request.POST)
        #check whether data is valid
        if form_instance.is_valid():
        #process data
               data=form_instance.cleaned_data
               w=data['weight']
               h=data['height']
               b=w/((h/100)**2)
               context={'result':b,'form':form_instance}
               return render(request,'bmi.html',context)

from app1.forms import SignupForm
class Signup(View):
    def get(self, request):
        form_instance = SignupForm()
        context = {'form': form_instance}
        return render(request, 'signup.html',context)
    def post(self, request):
            form_instance = SignupForm(request.POST)
            if form_instance.is_valid():
                data = form_instance.cleaned_data
                print(data)
                return render(request, 'sighnup.html')