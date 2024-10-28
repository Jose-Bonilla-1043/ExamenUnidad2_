from django.db import models

# Create your models here.

class Venta(models.Model):
    
    from django.db import models

class Venta(models.Model):
    id_venta = models.CharField(max_length=6, primary_key=True)
    fecha = models.DateField()
    estado = models.CharField(max_length=20)  
    cantidad = models.PositiveIntegerField()
    precio_total = models.PositiveIntegerField()

    def __str__(self):
        return self.id_venta
    