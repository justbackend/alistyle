from django.db import models
from userapp.models import Profile


class Bolim(models.Model):
    nom = models.CharField(max_length=150)
    rasm = models.FileField(upload_to="bolim")
    def __str__(self):
        return self.nom

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

class Izoh(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    matn = models.TextField()
    rating = models.IntegerField()
    sana = models.DateField()

    def __str__(self):
        return self.matn
