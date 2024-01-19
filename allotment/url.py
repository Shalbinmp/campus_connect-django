from django.conf.urls import url
from allotment import views

urlpatterns=[
    url('allotment/',views.allot),
    url('viewallo/',views.s_vw_allot),
]