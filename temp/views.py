from django.shortcuts import render

# Create your views here.



def admin_home(request):
    return render(request,'temp/index - Admin.html')


def student_home(request):
    return render(request,'temp/index - Student.html')


def teacher_home(request):
    return render(request,'temp/index - Teacher.html')


def login_home(request):
    return render(request,'temp/index - Home.html')


def admin_2_home(request):
    return render(request,'temp/admin_2_home.html')


def student_2_home(request):
    return render(request,'temp/student_2_home.html')


def teacher_2_home(request):
    return render(request,'temp/teacher_2_home.html')