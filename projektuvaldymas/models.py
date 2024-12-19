from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
from tinymce.models import HTMLField


class Klientas(models.Model):
    id = models.AutoField(primary_key=True)
    vardas = models.CharField("Vardas", max_length=100)
    pavarde = models.CharField("Pavardė", max_length=100)
    imone = models.CharField("Įmonė", max_length=250)
    kontaktai = models.CharField("Kontaktai", max_length=250)

    def __str__(self):
        return f"{self.vardas} {self.pavarde}"

    class Meta:
        verbose_name = "Klientas"
        verbose_name_plural = "Klientai"


class Darbuotojas(models.Model):
    id = models.AutoField(primary_key=True)
    vardas = models.CharField("Vardas", max_length=100)
    pavarde = models.CharField("Pavardė", max_length=100)
    pareigos = models.CharField("Pareigos", max_length=250)

    def __str__(self):
        return f"{self.vardas} {self.pavarde}, {self.pareigos}"

    class Meta:
        verbose_name = "Darbuotojas"
        verbose_name_plural = "Darbuotojai"


class Darbas(models.Model):
    pavadinimas = models.CharField("Pavadinimas", max_length=250)
    pastabos = models.TextField("Pastabos", max_length=1000)

    def __str__(self):
        return f"{self.pavadinimas}"

    class Meta:
        verbose_name = "Darbas"
        verbose_name_plural = "Darbai"


class Saskaita(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    israsymo_data = models.DateField("Išrašymo data", null=True, blank=True)
    suma = models.DecimalField("Suma", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.israsymo_data} - {self.suma}€"

    class Meta:
        verbose_name = "Saskaita"
        verbose_name_plural = "Saskaitos"


class Projektas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pavadinimas = models.CharField("Pavadinimas", max_length=250)
    pradzios_data = models.DateField("Pradžios data", default=timezone.now)
    pabaigos_data = models.DateField("Pabaigos data", null=True, blank=True)
    klientas = models.ForeignKey(Klientas, on_delete=models.CASCADE, related_name="projektai")
    vadovas = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vadovaujami_projektai")
    darbuotojai = models.ManyToManyField(Darbuotojas, related_name="projektai")
    darbai = models.ManyToManyField(Darbas, related_name="projektai")
    saskaitos = models.ManyToManyField(Saskaita, related_name="projektai")
    nuotrauka = models.ImageField(upload_to='projekto_nuotraukos/', blank=True, null=True)
    aprasymas = HTMLField(blank=True)

    def __str__(self):
        return f"{self.pavadinimas}"

    class Meta:
        verbose_name = "Projektas"
        verbose_name_plural = "Projektai"
