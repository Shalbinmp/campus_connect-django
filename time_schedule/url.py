from django.conf.urls import url
from time_schedule import views
urlpatterns = [
    url('time_schedule/', views.time_schedule),
    url('stvwtmsch/', views.st_vw_tmschedule),
    url('thvwtmsch/', views.th_vw_tmschedule),
]