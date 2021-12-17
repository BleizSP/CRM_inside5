from django.db import models


# Create your models here.
class Employees(models.Model):
    def __str__(self):
        return self.employees_name

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    employees_name = models.CharField(max_length=20)
    employees_lastname = models.CharField(max_length=20)
    employees_phone = models.IntegerField()
    employees_email = models.EmailField(max_length=20, null=True)
    employees_rank = models.CharField(max_length=20)
    employees_group = models.CharField(max_length=20)



