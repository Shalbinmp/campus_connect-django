from django.shortcuts import render
from feedback.models import Feedback
import datetime
# Create your views here.
def feed(request):
    ss = request.session["u_id"]
    if request.method=="POST":
        obj=Feedback()
        obj.feedback=request.POST.get('fbk')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.student_id=ss
        obj.save()
    return render(request,'feedback/feedback.html')

def ad_vw_feed(request):
    obj=Feedback.objects.all()
    context={
        'x':obj
    }
    return render(request,'feedback/ad_view_feedback.html',context)




def t_vw_feed(request):
    obj=Feedback.objects.all()
    context={
        'x':obj
    }
    return render(request,'feedback/te_view_feedback.html',context)