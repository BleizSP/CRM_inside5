from django.db import models


# Create your models here.


class Office(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=64)
    country = models.CharField(max_length=64)


class Menager(models.Model):
    def __str__(self):
        return self.Name + ' ' + self.lastname

    Name = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    phone = models.IntegerField()
    reg_time = models.DateField(auto_created=True)
    office = models.ForeignKey(Office, on_delete=models.CASCADE, related_name='offices')


class Employee(models.Model):
    def __str__(self):
        return self.name + " " + self.lastname

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employee'

    name = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    phone = models.IntegerField()
    email = models.EmailField(max_length=64, null=True)
    rank = models.CharField(max_length=20)
    group = models.CharField(max_length=20)
    reg_time = models.DateField(auto_now_add=True)


class Client(models.Model):
    def __str__(self):
        return self.name + " " + self.lastname

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Client'

    name = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    phone = models.DecimalField(max_digits=20, decimal_places=0)
    email = models.EmailField(max_length=64, null=True)
    salesman = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='salesman')
    retention = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='retention')
    reg_time = models.DateField(blank=True, null=True)


class Status(models.Model):
    def __str__(self):
        return self.status

    status = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'


class Bank(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=64)
    type = models.CharField(max_length=20)
    iban = models.CharField(max_length=128, blank=True, null=True)
    wallet = models.CharField(max_length=128, blank=True, null=True)
    owner = models.CharField(max_length=64, blank=True, null=True)
    swift = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    adres = models.TextField(max_length=128, blank=True, null=True)
    reg_date = models.DateField(blank=True, null=True)
    active = models.BooleanField()

    class Meta:
        verbose_name = 'Bank'
        verbose_name_plural = 'Banks'


class Operation(models.Model):
    def __str__(self):
        return self.client.name + ' ' + self.client.lastname + '  Cash: ' + str(self.cash)

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='operations')
    cash = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField(blank=True, null=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='bank')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='stat')
    who = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='ftd_employees', null=True, blank=True)
    type = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Operations'
        verbose_name_plural = 'Operations'
