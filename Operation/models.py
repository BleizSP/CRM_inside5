from django.db import models


# Create your models here.
class Status(models.Model):
    def __str__(self):
        return self.status

    status = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'


class Operation(models.Model):
    def __str__(self):
        return self.operation_client_id + " " + str(self.operation_client_cash)

    operation_client_id = models.CharField(max_length=10)
    operation_client_cash = models.DecimalField(max_digits=12, decimal_places=2)
    operation_date = models.DateField(blank=True, null=True)
    operation_bank = models.CharField(max_length=15, null=True)
    operation_status = models.ForeignKey(Status, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Operation'
        verbose_name_plural = 'Operations'

