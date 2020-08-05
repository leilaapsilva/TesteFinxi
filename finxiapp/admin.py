from django.contrib import admin

# Register your models here.

from finxiapp.models import DemandaDePecas, Anunciante
admin.site.register(DemandaDePecas)
admin.site.register(Anunciante)


