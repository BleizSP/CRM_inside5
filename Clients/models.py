from django.db import models


# Create your models here.
class Client(models.Model):
    def __str__(self):
        return self.client_name + " " + self.client_lastname

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    client_name = models.CharField(max_length=10)
    client_lastname = models.CharField(max_length=10)
    client_phone = models.DecimalField(max_digits=12, decimal_places=0)
    client_email = models.EmailField(max_length=20, null=True)
    client_salesman = models.CharField(max_length=20, null=True)
    client_reg_time = models.DateField(blank=True, null=True)
    client_bank = models.CharField(max_length=15, null=True)
