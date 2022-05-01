from django.db import models

# Create your models here.
class Alimento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    
    def __str__(self):
        alimento = "Nombre: " + self.nombre + " - " + "Categoría: " + self.categoria
        return alimento

class Plato(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tiempoPreparacion = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100, null=True)
    alimento = models.ManyToManyField(Alimento)

    def __str__(self):
        plato = "Plato: " + self.nombre + " - " + "Tiempo preparación: " + self.tiempoPreparacion + "Categoría: " + self.categoria + "Alimento: " + self.alimento
        return plato
