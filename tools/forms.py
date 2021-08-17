from django import forms
from tools import func
from tools import models


class Kanavka(forms.Form):
    D = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}), label="D", decimal_places=1)
    d = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}), label="d", decimal_places=1)
    L = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}), label="L", decimal_places=1)
    H = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}), label="H", decimal_places=1)
    R = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}), label="R", decimal_places=1)

class Rastochka(forms.Form):
    D = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}), label="D", decimal_places=1)
    d = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}), label="d", decimal_places=1)
    L = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}), label="L", decimal_places=1)
    a = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}), label="a", decimal_places=1)

class FormKanRezec(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "tt"}), label="Наименование", max_length=40)
    dmin = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}), label="d", decimal_places=1)
    ap = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}), label="ap", decimal_places=1)
    h = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}), label="h", decimal_places=1)
    r = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}), label="r", decimal_places=1)
    Lmax = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}), label="L", decimal_places=1)

class FormRastRezec(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "tt"}), label="Наименование", max_length=40)
    dmin = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}), label="d", decimal_places=1)
    ap = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}), label="ap", decimal_places=1)
    W = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}), label="W", decimal_places=1)
    Wp = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}), label="Wp", decimal_places=1)
    Lmax = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}), label="L", decimal_places=1)

class FormDelKan(forms.Form):
    ident = forms.ModelChoiceField(to_field_name="name",
                                    queryset=models.KanRezec.objects.all(),
                                    widget=forms.Select(attrs={"class": "dt"}),
                                    label="",
                                    empty_label="Выбрать резец")

class FormDelRast(forms.Form):
    ident = forms.ModelChoiceField(to_field_name="name",
                                    queryset=models.RastRezec.objects.all(),
                                    widget=forms.Select(attrs={"class": "dt"}),
                                    label="",
                                    empty_label="Выбрать резец")

class Password(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "pass"}),
                               initial="Пароль",
                               label="Пароль",
                               max_length=40)