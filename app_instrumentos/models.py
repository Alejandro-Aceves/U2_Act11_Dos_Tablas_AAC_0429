from django.db import models

# Create your models here.
from django.db import models

class Instrumento(models.Model):
    nombre = models.CharField(max_length=100, help_text="Nombre del instrumento")
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)
    foto_instrumento = models.ImageField(upload_to='img_instrumentos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Instrumento"
        verbose_name_plural = "Instrumentos"

class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    id_instrumento = models.ForeignKey('Instrumento', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_empresa} - Provee: {self.id_instrumento.nombre}"

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"