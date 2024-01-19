from django.conf.urls import url
from form import views
urlpatterns = [
    url('post_form_admin/', views.form_admin),
    url('ad_vw_frm/', views.ad_vw_form),
    url('th_vw_frm/', views.th_vw_form),
    url('form_pos_student/(?P<idd>\w+)',views.form_student),
    url('stu_vw_form/',views.stu_vw_form),
]