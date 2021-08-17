from django.shortcuts import render
from . import forms
from . import func
from tools import models

def index(request):
    return render(request,"index.html")


def kanavka(request):
    form = forms.Kanavka(request.POST)
    lst = []
    check = 0

    if request.method == "POST":
        if form.is_valid():
            database = models.KanRezec.objects.all()
            lst = func.check_kanavka(
                form.cleaned_data['D'],
                form.cleaned_data['d'],
                form.cleaned_data['L'],
                form.cleaned_data['H'],
                form.cleaned_data['R'],
                database
            )
            # если редактирование данных в БД,
            # то redirect либо на страницу редактирования, либо на какую-то иную
            # чтобы отменить эффект F5 с повторной отправкой формы и спамом БД.

            if not lst:
                check = 1

    return render(request, "tools/kanavka.html", {"form_kanavka": form, "lst": lst, "check": check})


def rast(request):
    if request.method == "POST":
        D = request.POST.get("D")
        d = request.POST.get("d")
        L = request.POST.get("L")
        a = request.POST.get("a")

        database = models.RastRezec.objects.all()
        lst = func.check_rastochka(D, d, L, a, database)
        form_rastochka = forms.Rastochka()
        check = 0
        if not lst:
            check = 1
        return render(request, "rast.html", {"form_rastochka": form_rastochka, "lst": lst, "check": check})
    else:
        form_rastochka = forms.Rastochka()
        lst = []
        check = 0
        return render(request, "rast.html", {"form_rastochka": form_rastochka, "lst": lst, "check": check})


def admin(request):
    return render(request,"admin.html")


def akan(request):
    if request.method == "POST":
        output = models.KanRezec.objects.all()
        password = request.POST.get("password")
        name = request.POST.get("name")
        check_pass = func.password(password)
        check = func.check_name(name, output)

        if not check_pass and not check:
            rezec = models.KanRezec()
            rezec.name = request.POST.get("name")
            rezec.dmin = request.POST.get("dmin")
            rezec.ap = request.POST.get("ap")
            rezec.h = request.POST.get("h")
            rezec.r = request.POST.get("r")
            rezec.Lmax = request.POST.get("Lmax")
            rezec.save()

            output = models.KanRezec.objects.all()
            form_akan = forms.FormKanRezec()
            form_password = forms.Password()
            post = {
                "form_akan": form_akan,
                "form_password": form_password,
                "output": output,
                "check": check,
                "check_pass": check_pass,
            }
            return render(request, "akan.html", post)

        form_akan = forms.FormKanRezec()
        form_password = forms.Password()
        post = {
            "form_akan": form_akan,
            "form_password": form_password,
            "output": output,
            "check": check,
            "check_pass": check_pass,
        }
        return render(request, "akan.html", post)
    else:
        output = models.KanRezec.objects.all()
        form_akan = forms.FormKanRezec()
        form_password = forms.Password()
        check = 0
        check_pass = 0
        post = {
            "form_akan": form_akan,
            "form_password": form_password,
            "output": output,
            "check": check,
            "check_pass": check_pass,
        }
        return render(request, "akan.html", post)


def arast(request):
    if request.method == "POST":
        output = models.RastRezec.objects.all()
        password = request.POST.get("password")
        name = request.POST.get("name")
        check_pass = func.password(password)
        check = func.check_name(name, output)

        if not check_pass and not check:
            rezec = models.RastRezec()
            rezec.name = request.POST.get("name")
            rezec.dmin = request.POST.get("dmin")
            rezec.ap = request.POST.get("ap")
            rezec.gugol = request.POST.get("W")
            rezec.ugol = request.POST.get("Wp")
            rezec.Lmax = request.POST.get("Lmax")
            rezec.save()

            output = models.RastRezec.objects.all()
            form_arast = forms.FormRastRezec()
            form_password = forms.Password()
            post = {
                "form_arast": form_arast,
                "form_password": form_password,
                "output": output,
                "check": check,
                "check_pass": check_pass,
            }
            return render(request, "arast.html", post)

        form_arast = forms.FormRastRezec()
        form_password = forms.Password()
        post = {
            "form_arast": form_arast,
            "form_password": form_password,
            "output": output,
            "check": check,
            "check_pass": check_pass,
        }
        return render(request, "arast.html", post)
    else:
        output = models.RastRezec.objects.all()
        form_arast = forms.FormRastRezec()
        form_password = forms.Password()
        check = 0
        check_pass = 0
        post = {
            "form_arast": form_arast,
            "form_password": form_password,
            "output": output,
            "check": check,
            "check_pass": check_pass,
        }
        return render(request, "arast.html", post)


def dkan(request):
    if request.method == "POST":
        password = request.POST.get("password")
        check_pass = func.password(password)

        if not check_pass:
            ident = request.POST.get("ident")
            rezec = models.KanRezec.objects.get(name=ident)
            rezec.delete()

            output = models.KanRezec.objects.all()
            form_dkan = forms.FormDelKan()
            form_password = forms.Password()
            post = {
                "form_dkan": form_dkan,
                "form_password": form_password,
                "output": output,
                "check_pass": check_pass,
            }
            return render(request, "dkan.html", post)

        output = models.KanRezec.objects.all()
        form_dkan = forms.FormDelKan()
        form_password = forms.Password()
        post = {
            "form_dkan": form_dkan,
            "form_password": form_password,
            "output": output,
            "check_pass": check_pass,
        }
        return render(request, "dkan.html", post)
    else:
        output = models.KanRezec.objects.all()
        form_dkan = forms.FormDelKan()
        form_password = forms.Password()
        check_pass = 0
        post = {
            "form_dkan": form_dkan,
            "form_password": form_password,
            "output": output,
            "check_pass": check_pass,
        }
        return render(request, "dkan.html", post)


def drast(request):
    if request.method == "POST":
        password = request.POST.get("password")
        check_pass = func.password(password)

        if not check_pass:
            ident = request.POST.get("ident")
            rezec = models.RastRezec.objects.get(name=ident)
            rezec.delete()

            output = models.RastRezec.objects.all()
            form_drast = forms.FormDelRast()
            form_password = forms.Password()
            post = {
                "form_drast": form_drast,
                "form_password": form_password,
                "output": output,
                "check_pass": check_pass,
            }
            return render(request, "drast.html", post)

        output = models.RastRezec.objects.all()
        form_drast = forms.FormDelRast()
        form_password = forms.Password()
        post = {
            "form_drast": form_drast,
            "form_password": form_password,
            "output": output,
            "check_pass": check_pass,
        }
        return render(request, "drast.html", post)
    else:
        output = models.RastRezec.objects.all()
        form_drast = forms.FormDelRast()
        form_password = forms.Password()
        check_pass = 0
        post = {
            "form_drast": form_drast,
            "form_password": form_password,
            "output": output,
            "check_pass": check_pass,
        }
        return render(request, "drast.html", post)