from django.db import models

class IntGroove(models.Model):
    name = models.CharField(max_length=40)
    dmin = models.DecimalField(decimal_places=1, max_digits=1000)
    ap = models.DecimalField(decimal_places=1, max_digits=1000)
    h = models.DecimalField(decimal_places=1, max_digits=1000)
    r = models.DecimalField(decimal_places=1, max_digits=1000)
    Lmax = models.DecimalField(decimal_places=1, max_digits=1000)

    def __str__(self):
        return self.name


class IntTurning(models.Model):
    name = models.CharField(max_length=40)
    dmin = models.DecimalField(decimal_places=1, max_digits=1000)
    ap = models.DecimalField(decimal_places=1, max_digits=1000)
    W = models.DecimalField(decimal_places=1, max_digits=1000)
    Wp = models.DecimalField(decimal_places=1, max_digits=1000)
    Lmax = models.DecimalField(decimal_places=1, max_digits=1000)

    def __str__(self):
        return self.name