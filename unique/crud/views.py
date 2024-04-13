from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import operation

def crud(request):
    emp = operation.objects.all()

    context = {
        'emp':emp,
    }

    return render(request,"crud.html",context)

def ADD(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = operation(
            name = name,
            email = email,
            address = address,
            phone = phone,
        )

        emp.save()
        return redirect('crud')
    
    return render(request,'crud.html') 

def Edit(request):
    emp = operation.objects.all()

    context = {
        'emp':emp,
    }

    return render(request,'crud.html',context)  

def Update(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone') 

        emp = operation(
            id = id,
            name = name,
            email = email,
            address = address,
            phone = phone,
        )

        emp.save()
        return redirect('crud')
    

    return render(request,'crud.html')

def Delete(request,id):
    emp = operation.objects.filter(id = id)
    emp.delete()

    context = {
        'emp':emp,
    }

    return redirect('crud')

def Add_page(request):
    emp = operation.objects.all()

    context = {
        'emp':emp,
    }

    return render(request,"manage_courses.html",context) 


def Manage_courses(request):
    emp = operation.objects.all()

    context = {
        'emp':emp,
    }

    return render(request,"manage_courses.html",context)        
    
                 