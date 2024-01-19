from django.conf.urls import url
from payment import views
urlpatterns = [
    url('payment/', views.payment),
    url('advwpt/', views.ad_vw_payment),
    url('thvwpay/', views.th_vw_viewpayment),
]