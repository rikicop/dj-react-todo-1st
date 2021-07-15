# todos/models.py
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title

class Constante(models.Model):
    valor = models.FloatField()
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.descripcion