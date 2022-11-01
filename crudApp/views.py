from django.shortcuts import render,HttpResponseRedirect
from .forms import studentRegister
from .models import student 


# Create your views here.

# this function will add new item and show all items 
def view(request):
    # if post request is sent by user
    if request.method == 'POST':
        fm = studentRegister(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = student(name=nm, email=em, password=pw)
            reg.save()
            fm = studentRegister()
    # if get request sent by user
    else:
        fm = studentRegister()

    userInfo = student.objects.all()
    return render(request,"view.html",{'form':fm,'stu':userInfo})

# this function will delete data 

def del_data(request, id):
    if request.method == 'POST':
        data_del = student.objects.get(pk=id)
        data_del.delete()
        return HttpResponseRedirect('/')


# this function will Update/Edit data 
def up_data(request,id):
    if request.method == 'POST':
        pi = student.objects.get(pk=id)
        fm = studentRegister(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = student.objects.get(pk=id)
        fm = studentRegister(instance=pi)
    return render(request,'update.html', {'form':fm})
      
