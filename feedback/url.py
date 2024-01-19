from django.conf.urls import url
from feedback import views
urlpatterns = [
    url('feedback/', views.feed),
    url('advwfeed/', views.ad_vw_feed),
    url('tvfeed/', views.ad_vw_feed),
]