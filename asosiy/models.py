from django.db import models



class Bolim(models.Model):
    nom = models.CharField(max_length=150)
    rasm = models.FileField(upload_to="bolim")

class Mahsulot(models.Model):
    nom = models.CharField(max_length=150)
    narx = models.PositiveBigIntegerField()
    chegirma = models.PositiveBigIntegerField()
    batafsil = models.TextField()
    brend = models.CharField(max_length=150)
    kafolat = models.IntegerField()
    yetkazish = models.IntegerField()
    mavjud = models.BooleanField(default=False)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)
    davlat = models.CharField(max_length=150)

class Media(models.Model):
    rasm = models.FileField()
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)

