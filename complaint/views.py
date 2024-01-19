from django.shortcuts import render
from complaint.models import Compliant
import datetime
# Create your views here.
def ad_vw_com(request):
    obj=Compliant.objects.all()
    context={
        'x':obj
    }
    return render(request,'complaint/ad_view_complaint.html',context)

def comp(request):
    ss = request.session["u_id"]
    if request.method=='POST':
        obj=Compliant()
        obj.complaint=request.POST.get('unm')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.reply="Pending"
        obj.student_id = ss
        obj.save()
    return render(request,'complaint/complaint.html')

def reply(request,idd):
    if request.method=='POST':
        obj = Compliant.objects.get(compliant_id=idd)
        obj.reply = request.POST.get('reply')
        obj.save()
        return ad_vw_com(request)
    return render(request,'complaint/reply.html')

def vwrply(request):
    ss = request.session["u_id"]
    obj=Compliant.objects.filter(student_id=ss)
    context={
        'x':obj
    }
    return render(request,'complaint/view_reply.html',context)