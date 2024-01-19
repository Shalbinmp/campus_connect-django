from django.conf.urls import url
from teacher import views
urlpatterns = [
    url('teacher/',views.teacher),

]