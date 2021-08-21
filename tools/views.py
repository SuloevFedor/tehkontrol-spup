from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from . import forms
from . import func
from . import models



def index(request):
    return render(request,"index.html")


def check_int_groove(request):
    form = forms.CheckIntGroove(request.POST)
    lst = []
    check = 0

    if request.method == "POST":
        if form.is_valid():
            database = models.IntGroove.objects.all()
            lst = func.check_int_groove(
                form.cleaned_data['D'],
                form.cleaned_data['d'],
                form.cleaned_data['L'],
                form.cleaned_data['H'],
                form.cleaned_data['R'],
                database
            )

            if not lst:
                check = 1

    return render(request, "tools/check_int_groove.html", {"form": form, "lst": lst, "check": check})


def check_int_turning(request):
    form = forms.CheckIntTurning(request.POST)
    lst = []
    check = 0

    if request.method == "POST":
        if form.is_valid():
            database = models.IntTurning.objects.all()
            lst = func.check_int_turning(
                form.cleaned_data['D'],
                form.cleaned_data['d'],
                form.cleaned_data['L'],
                form.cleaned_data['a'],
                database,
            )

            if not lst:
                check = 1

    return render(request, "tools/check_int_turning.html", {"form": form, "lst": lst, "check": check})


def login(request):
    form = forms.Password(request.POST)
    check = 0
    if request.method == "POST":
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
    #if user is None:
    #    check = 1
            if user is not None:
                login(request, user) #  !!!!! НЕ РАБОТАЕТ !!!!!!!
                return redirect('tools_index')

    return render(request,"tools/login.html", {"form": form, "check": check})


def tools_index(request):
    return render(request, "tools/index.html")


def add_int_groove(request):
    form = forms.AddIntGroove(request.POST)
    output = models.IntGroove.objects.all()
    check = 0

    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data['name']
            check = func.check_name(name, output)

            if not check:
                tool = models.IntGroove()
                tool.name = form.cleaned_data['name']
                tool.dmin = form.cleaned_data['dmin']
                tool.ap = form.cleaned_data['ap']
                tool.h = form.cleaned_data['h']
                tool.r = form.cleaned_data['r']
                tool.Lmax = form.cleaned_data['Lmax']
                tool.save()

                output = models.IntGroove.objects.all()

    return render(request, "tools/add_int_groove.html", {"form": form, "output": output, "check": check,})


def add_int_turning(request):
    form = forms.AddIntTurning(request.POST)
    output = models.IntTurning.objects.all()
    check = 0

    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data['name']
            check = func.check_name(name, output)

            if not check:
                tool = models.IntTurning()
                tool.name = form.cleaned_data['name']
                tool.dmin = form.cleaned_data['dmin']
                tool.ap = form.cleaned_data['ap']
                tool.W = form.cleaned_data['W']
                tool.Wp = form.cleaned_data['Wp']
                tool.Lmax = form.cleaned_data['Lmax']
                tool.save()

                output = models.IntTurning.objects.all()

    return render(request, "tools/add_int_turning.html", {"form": form, "output": output, "check": check, })


def del_int_groove(request):
    form = forms.DelIntGroove(request.POST)
    output = models.IntGroove.objects.all()

    if request.method == "POST":
        if form.is_valid():
            #ident = request.POST.get("ident")
            name = form.cleaned_data['name']
            tool = models.IntGroove.objects.get(name=name)
            tool.delete()

            output = models.IntGroove.objects.all()

    return render(request, "tools/del_int_groove.html", {"form": form, "output": output})


def del_int_turning(request):
    form = forms.DelIntTurning(request.POST)
    output = models.IntTurning.objects.all()

    if request.method == "POST":
        if form.is_valid():
            # ident = request.POST.get("ident")
            name = form.cleaned_data['name']
            tool = models.IntTurning.objects.get(name=name)
            tool.delete()

            output = models.IntTurning.objects.all()

    return render(request, "tools/del_int_turning.html", {"form": form, "output": output})