from django.shortcuts import render, redirect

from .forms import *
from .models import *

def hamma_fanlar(req):
    if req.method == "POST":
        forma = FanForm(req.POST)
        if forma.is_valid():
            forma.save()
    return redirect('/hamma_fanlar/')

    natija = Fan.objects.all()
    kiritilgan_nom = req.GET.get("nomi")
    if kiritilgan_nom is not None:
        natija = Fan.objects.filter(nom__contains=kiritilgan_nom)
    data ={
        "fanlar": natija
    }
    return render(req,"fan.html",data)



def hamma_yonalish(req):
    if req.method == "POST":
        forma = YonalishForm(req.POST)
        if forma.is_valid():
            forma.save()

    return redirect('/hamma_yonalishlar/')

    natija = Yonalish.objects.all()
    kiritilgan_nom = req.GET.get("nomi")
    if kiritilgan_nom is not None:
        natija = Yonalish.objects.filter(nom__contains=kiritilgan_nom)
    data ={
        "yonalish": natija
    }
    return render(req,"yonalish.html",data)


def hamma_ustoz(req):
    if req.method == "POST":
        forma =UstozForm(req.POST)
        if forma.is_valid():
            forma.save()

    return redirect('/hamma_ustozlar/')

    natija = Ustoz.objects.all()
    kiritilgan_ism = req.GET.get("ismi")
    if kiritilgan_ism is not None:
        natija = Ustoz.objects.filter(ism__contains=kiritilgan_ism)
    data = {
        "ustoz": natija
    }
    return render(req, "ustoz.html", data)


"Update"
"4 masala"

def fan_update(request,pk):
    if request.method == "POST":
        Fan.objects.filter(id=pk).update(
            nom = request.POST.get("nomi"),
            yonalish = Yonalish.objects.get(id=request.POST.get("yonalish")),
            asosiy = request.POST.get("asosiy")
        )
        return redirect('/fanlar/')
    content = {
        "fan": Fan.objects.get(id=pk),
        "yonalish": Yonalish.objects.all()
    }
    return render(request,"fan_update.html",content)

"5 masala"

def yonalish_update(request,pk):
    if request.method == "POST":
        Yonalish.objects.filter(id=pk).update(
            nom = request.POST.get("nomi"),
            aktiv = request.POST.get("aktiv"),
        )
        return redirect('/yonalishlar/')
    content = {
        "yonalish": Yonalish.objects.get(id=pk),
    }
    return render(request,"yonalish_update.html",content)



"6 masala"


def ustoz_update(request,pk):
    if request.method == "POST":
        Ustoz.objects.filter(id=pk).update(
            ism = request.POST.get("ismi"),
            jins = request.POST.get("jinsi"),
            yosh = request.POST.get("yosh"),
            daraja = request.POST.get("daraja"),
            fan = Fan.objects.get(id=request.POST.get("fan"))
        )
        return redirect('/ustozlar/')
    content = {
        "ustoz": Ustoz.objects.get(id=pk),
        "fan": Fan.objects.all()
    }
    return render(request,"ustoz_update.html",content)


