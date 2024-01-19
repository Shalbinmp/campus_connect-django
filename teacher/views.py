from django.shortcuts import render
from teacher.models import Teacher
from login.models import Login
# Create your views here.
def teacher(request):
    if request.method=="POST":
        obj=Teacher()
        obj.name=request.POST.get('nm')
        obj.mobile_number=request.POST.get('mbn')
        obj.department=request.POST.get('dpt')
        obj.password=request.POST.get('psw')
        obj.save()
        ob = Login()
        ob.username = obj.name
        ob.password = obj.password
        ob.u_id =obj.teacher_id
        ob.type = 'teacher'
        ob.save()
    return render(request,'teacher/Register teacher.html')

