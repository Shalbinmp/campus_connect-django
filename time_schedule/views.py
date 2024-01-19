from django.shortcuts import render
from time_schedule.models import TimeSchedule

# Create your views here.
def time_schedule(request):
    if request.method=="POST":
        obj=TimeSchedule()
        obj.time=request.POST.get('tm')
        obj.date=request.POST.get('dt')
        obj.save()
    return render(request,'time_schedule/Schedule.html')

def st_vw_tmschedule(request):
    obj=TimeSchedule.objects.all()
    context={
        'x':obj
    }
    return render(request,'time_schedule/st_vw_time schedule.html',context)

def th_vw_tmschedule(request):
    obj=TimeSchedule.objects.all()
    context={
        'x':obj
    }
    return render(request,'time_schedule/th_vw_time schedule.html',context)