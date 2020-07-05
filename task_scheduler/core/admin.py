from django.contrib import admin
from task_scheduler.core.models import Numero

class NumeroModelAdmin(admin.ModelAdmin):
    list_display = ('numero',)


admin.site.register(Numero, NumeroModelAdmin)

