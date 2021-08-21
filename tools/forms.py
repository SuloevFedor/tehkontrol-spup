from django import forms
from . import models


class CheckIntGroove(forms.Form):
    D = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}),
                           label="D",
                           decimal_places=1,
                           min_value=0,
                           )
    d = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}),
                           label="d",
                           decimal_places=1,
                           min_value=0,
                           )
    L = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}),
                           label="L",
                           decimal_places=1,
                           min_value=0,
                           )
    H = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}),
                           label="H",
                           decimal_places=1,
                           min_value=0,
                           )
    R = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}),
                           label="R",
                           decimal_places=1,
                           min_value=0,
                           )


class CheckIntTurning(forms.Form):
    D = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}),
                           label="D",
                           decimal_places=1,
                           min_value=0,
                           )
    d = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}),
                           label="d",
                           decimal_places=1,
                           min_value=0,
                           )
    L = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}),
                           label="L",
                           decimal_places=1,
                           min_value=0,
                           )
    a = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}),
                           label="a",
                           decimal_places=1,
                           min_value=0,
                           )


class AddIntGroove(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "tt"}), label="Наименование", max_length=40)
    dmin = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}),
                              label="d",
                              decimal_places=1,
                              min_value=0,
                              max_value=1000,
                              )
    ap = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}),
                            label="ap",
                            decimal_places=1,
                            min_value=0,
                            max_value=1000,
                            )
    h = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}),
                           label="h",
                           decimal_places=1,
                           min_value=0,
                           max_value=1000,
                           )
    r = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}),
                           label="r",
                           decimal_places=1,
                           min_value=0,
                           max_value=1000,
                           )
    Lmax = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}),
                              label="L",
                              decimal_places=1,
                              min_value=0,
                              max_value=1000,
                              )


class AddIntTurning(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "tt"}), label="Наименование", max_length=40)
    dmin = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}),
                              label="d",
                              decimal_places=1,
                              min_value=0,
                              max_value=1000,
                              )
    ap = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}),
                            label="ap",
                            decimal_places=1,
                            min_value=0,
                            max_value=1000,
                            )
    W = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}),
                           label="W",
                           decimal_places=1,
                           min_value=0,
                           max_value=1000,
                           )
    Wp = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}),
                            label="Wp",
                            decimal_places=1,
                            min_value=0,
                            max_value=1000,
                            )
    Lmax = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "ff"}),
                              label="L",
                              decimal_places=1,
                              min_value=0,
                              max_value=1000,
                              )

class DelIntGroove(forms.Form):
    name = forms.ModelChoiceField(to_field_name="name",
                                    queryset=models.IntGroove.objects.all(),
                                    widget=forms.Select(attrs={"class": "dt"}),
                                    label="",
                                    empty_label="Выбрать резец"
                                  )

class DelIntTurning(forms.Form):
    name = forms.ModelChoiceField(to_field_name="name",
                                    queryset=models.IntTurning.objects.all(),
                                    widget=forms.Select(attrs={"class": "dt"}),
                                    label="",
                                    empty_label="Выбрать резец"
                                  )


class Password(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "tt"}), label="Имя", max_length=40)
    password = forms.CharField(widget=forms.TextInput(attrs={"class": "tt"}), label="Пароль", max_length=40)


""" 
    username = forms.CharField(widget=forms.PasswordInput(attrs={"class": "pass"}),
                            initial="Имя",
                            label="Имя",
                            max_length=40
                           )
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "pass"}),
                               initial="Пароль",
                               label="Пароль",
                               max_length=40
                               )"""