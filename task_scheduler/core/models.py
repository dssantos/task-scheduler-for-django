from django.db import models

class Numero(models.Model):
    numero = models.IntegerField()

    def __str__(self):
        return str(self.numero)

