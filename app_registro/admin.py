from django.contrib import admin
from .models import Conferencia, Conferencista
# Register your models here.

class ConferenciaAdmin(admin.ModelAdmin):
    list_display=('nombres','fecha','hora','conferencista')

admin.site.register(Conferencia,ConferenciaAdmin)
admin.site.register(Conferencista)