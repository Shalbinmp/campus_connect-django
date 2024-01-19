from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from student.models import Student
from login.models import Login
from login import views
# Create your views here.
def student(request):
    if request.method=="POST":
        obj=Student()
        obj.register_id=request.POST.get('rnm')
        obj.username=request.POST.get('unm')
        obj.password=request.POST.get('psw')
        # obj.course_id=1
        obj.save()
        ob = Login()
        ob.username =obj.username
        ob.password = obj.password
        ob.u_id = obj.student_id
        ob.type = 'student'
        ob.save()
        return HttpResponseRedirect('/login/login/')
    return render(request,'student/student.html')

