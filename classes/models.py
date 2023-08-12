from django.db import models

# Create your models here.
class Classe(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to = 'classe', blank=True)

    def __str__(self):
        return self.nom

class Eleve(models.Model):
    nom = models.CharField(max_length=100)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Cours(models.Model):
    nom = models.CharField(max_length=100)
    chapitre = models.TextField(max_length=500)
    eleve = models.ManyToManyField(Eleve)

    def __str__(self):
        return self.nom
