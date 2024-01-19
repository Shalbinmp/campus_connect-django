from django.shortcuts import render
from allotment.models import Allotment
# Create your views here.

def allot(request):
    if request.method=='POST':
        obj=Allotment()
        obj.cap_id=request.POST.get('cid')
        obj.name=request.POST.get('nm')
        obj.address=request.POST.get('Address')
        obj.age=request.POST.get('age')
        obj.dob=request.POST.get('dob')
        obj.mobile_number=request.POST.get('mbn')
        obj.save()
    return render(request,'allotment/Allotment.html')

def s_vw_allot(request):
    obj=Allotment.objects.all()
    context={
        'x':obj
    }
    return render(request,'allotment/st_view_allotment.html',context)