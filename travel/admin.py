from django.contrib import admin
from travel import models

@admin.register(models.TCTUsers)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')
# Register your models here.
