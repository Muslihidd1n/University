from django.db import models

gender =[
    ("Erkak" , "Erkak"),
    ("Ayol" , "Ayol")
]


daraja = [
    ("Bakalavr" , "Bakalavr" ),
    ("Magistr" , "Magistr")]


# Universtitet


class Yonalish(models.Model):
    nom = models.CharField(max_length=30)
    aktiv = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nom}'



class Fan(models.Model):
    nom = models.CharField(max_length=30)
    yonalish = models.ForeignKey(Yonalish , on_delete=models.CASCADE)
    asosiy = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nom}'


class Ustoz(models.Model):
    ism = models.CharField(max_length=30)
    jins = models.CharField(max_length=30 , choices=gender)
    yosh = models.PositiveSmallIntegerField()
    daraja = models.CharField(max_length=30 , choices=daraja)
    fan = models.ForeignKey(Fan , on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.ism}'
