from django.db import models


class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    facultad = models.CharField(max_length=100)
    duracion = models.PositiveIntegerField()
    
    MODALIDAD_CHOICES = [
        ('Presencial', 'Presencial'),
        ('Online', 'Online'),
        ('Híbrida', 'Híbrida'),
    ]
    
    modalidad = models.CharField(
        max_length=20,
        choices=MODALIDAD_CHOICES
    )

    JORNADA_CHOICES = [
        ('Diurna', 'Diurna'),
        ('Vespertina', 'Vespertina'),
    ]

    jornada = models.CharField(
        max_length=20,
        choices=JORNADA_CHOICES
    )

    arancel = models.DecimalField(
        max_digits=10,
        decimal_places=0
    )

    cupos = models.PositiveIntegerField()
    correo = models.EmailField()

    def __str__(self):
        return self.nombre