from django.shortcuts import render,HttpResponseRedirect
from enroll.models import *
from enroll.forms import *
# Create your views here.

#this function will add new item and show all item
def show(request):
    if request.method == 'POST':
        fm=Student(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            ps=fm.cleaned_data['password']
            reg=user(name=nm,email=em,password=ps)
            reg.save()
            fm=Student()
    else:
        fm=Student()    
    stud=user.objects.all()
    return render(request,'show.html',{'form':fm,'stu':stud})
#this function will uptade/edit
def update_data(request,id):
    if request.method=='POST':
        pi=user.objects.get(pk=id)
        fm=Student(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=user.objects.get(pk=id)
        fm=Student(instance=pi)
    return render(request,'update.html',{'form':fm})

#This function will delete
def delete_data(request,id):
    if request.method=='POST':
        pi=user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')