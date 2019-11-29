from django.shortcuts import render, redirect
from festival.models import Festival
from django.contrib import messages

def register(request):
  if request.method =="POST":
    name = request.POST.get("fes_name", " ")
    date = request.POST.get("fes_date", " ")
    place = request.POST.get("fes_loca", " ")
    price = request.POST.get("fes_price", " ")
    picture = request.POST.get("fes_pic", " ")

    is_festival_in = Festival.objects.filter(name=name)
    if is_festival_in.count() == 0: 
      fest = Festival(name=name, date=date, place=place, price=price, pic=picture)
      fest.save()
    else:
      messages.info(request, "등록하려 하는 축제 정보가 이미 DB안에 존재합니다!")
      return redirect('/manager/register_festival')

    messages.info(request, "등록되었습니다")
    return redirect('/index')
  else:
    return render(request, 'createFestival.html')

def confirm(request):
  if reqeust.method=="POST":
  
    return redirect('/manager/confirm_ticket')
  else:
    
    return render(request, 'confirmTicket.html', context)