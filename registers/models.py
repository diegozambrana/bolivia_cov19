from django.db import models


class Departamento(models.Model):
    nombre = models.CharField(max_length=20)
    codigo = models.CharField(max_length=5)

    def __str__(self):
        return "[ {} ] - {}".format(self.codigo, self.nombre,)

    class Meta:
        unique_together = ['nombre', 'codigo']


class Registro(models.Model):
    fecha = models.DateField()
    departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE,
                                     null=True, blank=True)
    confirmados = models.IntegerField(default=0, null=True, blank=True)
    decesos = models.IntegerField(default=0, null=True, blank=True)
    recuperados = models.IntegerField(default=0, null=True, blank=True)
    sospechosos = models.IntegerField(default=0, null=True, blank=True)
    descartados = models.IntegerField(default=0, null=True, blank=True)
    total = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return "[{}] - {}".format(self.departamento.codigo, self.fecha)
