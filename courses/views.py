from django.shortcuts import render
from courses.models import Courses
# Create your views here.
def courses(request):
    if request.method=='POST':
        obj=Courses()
        obj.course=request.POST.get('cors')
        obj.save()
    return render(request,'courses/courses.html')

def st_vw_courses(request):
    obj=Courses.objects.all()
    context={
        'x':obj
    }
    return render(request,'courses/st_view_courses.html',context)

def th_vw_course(request):
    obj=Courses.objects.all()
    context={
        'x':obj
    }
    return render(request,'courses/th_vw_course.html',context)