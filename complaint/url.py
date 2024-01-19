from django.conf.urls import url
from complaint import views


urlpatterns = [
    url('complaint/', views.comp),
    # url('vw_rply/', views.vwrply),
    url('ad_vw_comp/',views.ad_vw_com),
    url('reply/(?P<idd>\w+)',views.reply),
]