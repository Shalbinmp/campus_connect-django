from django.shortcuts import render
from notification.models import Notifiction
import datetime
# Create your views here.
def notification(request):
    if request.method=="POST":
        obj=Notifiction()
        obj.notification=request.POST.get('ntf')
        obj.date = datetime.datetime.today()
        obj.time = datetime.datetime.now()
        obj.save()
    return render(request,'notification/notification.html')

def st_vw_notification(request):
    obj=Notifiction.objects.all()
    context={
        'x':obj
    }
    return render(request,'notification/st_view_notification.html',context)

def ad_vw_notification(request):
    obj=Notifiction.objects.all()
    context={
        'x':obj
    }
    return render(request,'notification/ad_vw_notification.html',context)