from django.db import models


# Create your models here.
# def custom_upland_to(instance, filename):
#     old_instance = Consumption.objects.get(pk=instance.pk)
#     old_instance.imagen.delete()
#     return 'consumptions/' + filename


class Consumption(models.Model):
    id = models.AutoField(primary_key=True)
    odometro = models.BigIntegerField(verbose_name="Odometro", default=0)
    monto = models.FloatField(verbose_name="Monto", default=0)
    precio_litro = models.FloatField(verbose_name="Precio X Litro", default=0)
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha De Ingreso")
    boleta = models.BigIntegerField(default=0, verbose_name="Numero Boleta")
    imagen = models.ImageField(upload_to="media/", null=True,
                               blank=True,
                               verbose_name="Imagen")
    class Meta:
        verbose_name = "Consumo"
        verbose_name_plural = "Consumos"
        ordering = ['id']

    # def _get_total_odometro(self, Consumption):
    #     return self.Consumption.objects.last('odometro') - self.Consumption.objects.first('odometro')

    # total = property(_get_total_odometro)

    def __str__(self):
        return str(self.boleta)
