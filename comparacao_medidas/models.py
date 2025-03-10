# models.py

from django.db import models

class MedidasCliente(models.Model):
    ombro = models.DecimalField(max_digits=5, decimal_places=2)
    torax = models.DecimalField(max_digits=5, decimal_places=2)
    cintura = models.DecimalField(max_digits=5, decimal_places=2)
    quadril = models.DecimalField(max_digits=5, decimal_places=2)
    comprimento_manga = models.DecimalField(max_digits=5, decimal_places=2)
    comprimento_perna = models.DecimalField(max_digits=5, decimal_places=2)

class TabelaMedidas(models.Model):
    nome = models.CharField(max_length=255)
    ombro = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    torax = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    cintura = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    quadril = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    comprimento_manga = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    comprimento_perna = models.DecimalField(max_digits=5, decimal_places=2, blank=True)

    def __str__(self):
        return self.nome

class TabelaMedidasCalca(models.Model):
    nome = models.CharField(max_length=255)
    ombro = models.DecimalField(max_digits=5, decimal_places=2)
    torax = models.DecimalField(max_digits=5, decimal_places=2)
    cintura = models.DecimalField(max_digits=5, decimal_places=2)
    quadril = models.DecimalField(max_digits=5, decimal_places=2)
    comprimento_manga = models.DecimalField(max_digits=5, decimal_places=2)
    comprimento_perna = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome


class TabelaMedidasJaqueta(models.Model):
    nome = models.CharField(max_length=255)
    ombro = models.DecimalField(max_digits=5, decimal_places=2)
    torax = models.DecimalField(max_digits=5, decimal_places=2)
    cintura = models.DecimalField(max_digits=5, decimal_places=2)
    quadril = models.DecimalField(max_digits=5, decimal_places=2)
    comprimento_manga = models.DecimalField(max_digits=5, decimal_places=2)
    comprimento_perna = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome