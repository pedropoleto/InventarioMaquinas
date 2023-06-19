from django.db import models

class Maquinas(models.Model):
    tipo_choices = (
        ("Windows 7", 'Windows 7'),
        ("Windows 10", 'Windows 10'),
        ("Windows 11", 'Windows 11'),
        ("Server", 'Server')
    )

    usuario = models.CharField(max_length=50)
    patrimonio = models.CharField(max_length=50)
    sistema = models.CharField(choices=tipo_choices, max_length=50)