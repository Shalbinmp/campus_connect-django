from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from form.models import Forms
# Create your views here.
def form_admin(request):
    if request.method=="POST":
        obj=Forms()
        obj.type = request.POST.get('type')
        obj.submited_form = 'not submited'
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.admin_form = myfile.name
        obj.save()
    return render(request,'form/admin_postform.html')

def form_student(request,idd):
    if request.method=="POST":
        obj=Forms.objects.get(forms_id=idd)
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.submited_form = myfile.name
        obj.save()
        return HttpResponseRedirect('/form/stu_vw_form/')
    return render(request,'form/post_student_form.html')

def th_vw_form(request):
    obj=Forms.objects.all()
    context={
        'x':obj
    }
    return render(request,'form/th_vw_filledform.html',context)

def ad_vw_form(request):
    obj=Forms.objects.all()
    context={
        'x':obj
    }
    return render(request, 'form/admin_view_form.html', context)


def stu_vw_form(request):
    obj=Forms.objects.all()
    context={
        'x':obj
    }
    return render(request, 'form/stu_vw_form.html', context)