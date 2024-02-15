from django.shortcuts import render,redirect
from django.contrib import messages
from .form import register
from .models import student
def enroll(request):
    if request.method=='POST':
        fm=register(request.POST)
        if fm.is_valid():
            fm.save()
            valname=fm.cleaned_data['name']
            messages.success(request,f'New Student,{valname} is added!!')
            return redirect('/')
    else:
        fm=register()
    data=student.objects.all()
    return render(request,'enroll.html',{'form':fm,'data':data})

def edit(request,id):
    all_data=student.objects.all()
    data=student.objects.get(id=id)
    if request.method=='POST':
        fm=register(request.POST,instance=data)
        if fm.is_valid():
            valname=fm.cleaned_data['name']
            fm.save()
            messages.success(request,f'{valname} is Updated.')
            return redirect('/') 
    else:
        fm=register(instance=data)
    return render(request,'enroll.html',{'form':fm,'data':all_data})
        
def delete(request,id):
    if request.method=='POST':
        data=student.objects.get(id=id)
        valname=data.name
        data.delete()
        messages.error(request,f'{valname} has been deleted successfully!!')
        return redirect('/')
        
    