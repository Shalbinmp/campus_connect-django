from django.conf.urls import url
from notification import views
urlpatterns = [
    url('notification/', views.notification),
    url('advwntf/', views.ad_vw_notification),
    url('stvwntf/', views.st_vw_notification),
]