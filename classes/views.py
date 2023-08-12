from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Classe, Eleve, Cours

def classes(request):
    classes = Classe.objects.all()
    return render(request, 'classes/classes.html', {'classes': classes})

def eleves(request, classe_id):
    classe = Classe.objects.get(pk=classe_id)
    eleves = classe.eleve_set.all()
    for eleve in eleves:
        eleve.nombre_cours = eleve.cours_set.count()
    return render(request, 'eleves/eleves.html', {'classe': classe, 'eleves': eleves})

def cours(request, eleve_id):
    eleve = Eleve.objects.get(pk=eleve_id)
    cours = eleve.cours_set.all()
    return render(request, 'cours/cours.html', {'eleve': eleve, 'cours': cours})
