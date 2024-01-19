from django.conf.urls import url
from student import views
urlpatterns = [
    url('student/',views.student),

]