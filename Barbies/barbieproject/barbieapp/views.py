#
from django.shortcuts import render, redirect
from . models import cutie
from .forms import barbieform
# Create your views here.
def copying(request):
    beauty=cutie.objects.all()
    context={
        'smile_list':beauty
    }
    return render(request,'index.html',context)
def detail(request, barb_id,):
    beauty=cutie.objects.get(id=barb_id)
    return render(request,'detail.html',{'ken':beauty})

def add(request):
    if request.method=="POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        style = request.POST.get('style')
        img = request.FILES['img']
        barbie = cutie(name=name,price=price,style=style,img=img)
        barbie.save()
        return redirect('/')
    return render(request,'adding.html')

def update(request,id):
    res=cutie.objects.get(id=id)
    form=barbieform(request.POST or None,request.FILES,instance=res)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'res':res })
def edit(request,id):
    res=cutie.objects.get(id=id)
    form=barbieform(request.POST or None,request.FILES,instance=res)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'res':res})

def deleted(request,id):
    if request.method=="POST":
        dele = cutie.objects.get(id=id)
        dele.delete()
        return redirect('/')
    return render(request,'deleted.html')

