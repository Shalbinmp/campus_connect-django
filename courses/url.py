from django.conf.urls import url
from courses import views
urlpatterns = [
    url('courses/', views.courses),
    url('stvwcrs/', views.st_vw_courses),
    url('thvwcrs/', views.th_vw_course),
]