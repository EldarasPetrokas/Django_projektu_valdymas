from django.contrib import admin
from .models import Klientas, Darbuotojas, Darbas, Saskaita, Projektas
from tinymce.widgets import TinyMCE
from django.db import models

class DarbasAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'pastabos')


class DarbuotojasAdmin(admin.ModelAdmin):
    # Metodas skirtas admin puslapyje atvaizduoti varda ir pavarde kartu
    def pilnas_vardas(self, obj):
        return f"{obj.vardas} {obj.pavarde}"

    pilnas_vardas.short_description = "Vardas, Pavarde"  # Sitaip bus atvaizduojama admin puslapyje

    list_display = ('id', 'pilnas_vardas', 'pareigos')


class KlientasAdmin(admin.ModelAdmin):
    def pilnas_vardas(self, obj):
        return f"{obj.vardas} {obj.pavarde}"

    pilnas_vardas.short_description = "Vardas, Pavarde"
    list_display = ('id', 'pilnas_vardas', 'imone', 'kontaktai')
    list_filter = ('id', 'imone', 'kontaktai')


class ProjektasAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
    list_display = ('pavadinimas', 'vadovas', 'pradzios_data', 'pabaigos_data')



class SaskaitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'israsymo_data', 'suma')
    list_filter = ('israsymo_data', 'suma')


admin.site.register(Klientas, KlientasAdmin)
admin.site.register(Darbuotojas, DarbuotojasAdmin)
admin.site.register(Darbas, DarbasAdmin)
admin.site.register(Saskaita, SaskaitaAdmin)
admin.site.register(Projektas, ProjektasAdmin)
