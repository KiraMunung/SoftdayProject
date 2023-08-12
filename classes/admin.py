from django.contrib import admin

# Register your models here.

from .models import Classe, Eleve, Cours

class ClasseAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom']


class EleveAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom']

class CoursAdmin(admin.ModelAdmin):
    list_display = ('nom', 'chapitre')
    search_fields = ['nom']

admin.site.register(Classe, ClasseAdmin)
admin.site.register(Eleve, EleveAdmin)
admin.site.register(Cours, CoursAdmin)
