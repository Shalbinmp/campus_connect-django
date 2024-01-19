from django.shortcuts import render
from payment.models import Payment


# Create your views here.
def payment(request):
    ss = request.session["u_id"]
    if request.method=="POST":
        obj=Payment()
        obj.cvv=request.POST.get('cvv')
        obj.amount=request.POST.get('amt')
        obj.card_holder_name=request.POST.get('cdm')
        obj.card_number=request.POST.get('cnm')
        obj.upi=request.POST.get('upi')
        obj.net_banking=request.POST.get('ntb')
        obj.student_id=ss
        obj.save()

    return render(request,'payment/payment.html')

def ad_vw_payment(request):
    obj=Payment.objects.all()
    context={
        'x':obj
    }
    return render(request,'payment/ad_vw_payment.html',context)

def th_vw_viewpayment(request):
    obj=Payment.objects.all()
    context={
        'x':obj
    }
    return render(request,'payment/th_vw_viewpayment.html',context)