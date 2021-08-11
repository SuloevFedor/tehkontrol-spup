from django.db import models

class KanRezec(models.Model):
    name = models.CharField(max_length=40)
    dmin = models.DecimalField(decimal_places=1, max_digits=1000)
    ap = models.DecimalField(decimal_places=1, max_digits=1000)
    h = models.DecimalField(decimal_places=1, max_digits=1000)
    r = models.DecimalField(decimal_places=1, max_digits=1000)
    Lmax = models.DecimalField(decimal_places=1, max_digits=1000)

    def __str__(self):
        return self.name


class RastRezec(models.Model):
    name = models.CharField(max_length=40)
    dmin = models.DecimalField(decimal_places=1, max_digits=1000)
    ap = models.DecimalField(decimal_places=1, max_digits=1000)
    gugol = models.DecimalField(decimal_places=1, max_digits=1000)
    ugol = models.DecimalField(decimal_places=1, max_digits=1000)
    Lmax = models.DecimalField(decimal_places=1, max_digits=1000)

    def __str__(self):
        return self.name