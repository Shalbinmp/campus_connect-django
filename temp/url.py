from django.conf.urls import url
from . import views

urlpatterns = [
    url('admin/',views.admin_home),
    url('login/',views.login_home),
    url('student/',views.student_home),
    url('teacher/',views.teacher_home),
    url('std2_home/',views.student_2_home),
    url('tchr_home/',views.teacher_2_home),
    url('admn_home/',views.admin_2_home),
]