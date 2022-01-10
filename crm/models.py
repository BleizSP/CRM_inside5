from django.db import models

# Create your models here.
from django.db.models import Sum, Count


class Office(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=64)
    country = models.CharField(max_length=64)

    @property
    def employee_list(self):
        emplo_office_list = Employee.objects.filter(office_id=self)
        return emplo_office_list

    @property
    def employee_count(self):
        emplo_office_stats = Employee.objects.filter(office_id=self).count()
        if emplo_office_stats is None:
            emplo_office_stats = 0
        return emplo_office_stats

    @property
    def client_count(self):
        client_office_stats = Client.objects.filter(office_id=self).filter(active=True).count()
        if client_office_stats is None:
            client_office_stats = 0
        return client_office_stats

    @property
    def client_ammount_ftd(self):
        ftd_office_stats = Operation.objects.filter(
            client__office_id=self).filter(status_id=5).filter(type_id=4).aggregate(Sum('cash')).get('cash__sum')
        if ftd_office_stats is None:
            ftd_office_stats = 0
        return ftd_office_stats

    @property
    def client_ammount_redepo(self):
        redepo_office_stats = Operation.objects.filter(
            client__office_id=self).filter(status_id=5).filter(type_id=2).aggregate(Sum('cash')).get('cash__sum')
        if redepo_office_stats is None:
            redepo_office_stats = 0
        return redepo_office_stats

    @property
    def client_ammount_wd(self):
        wd_office_stats = Operation.objects.filter(
            client__office_id=self).filter(status_id=5).filter(type_id=3).aggregate(Sum('cash')).get('cash__sum')
        if wd_office_stats is None:
            wd_office_stats = 0
        return wd_office_stats

    @property
    def client_ammount_bilans(self):
        depo = Operation.objects.filter(
            client__office_id=self).filter(status_id=5).aggregate(Sum('cash')).get('cash__sum')
        wd = Operation.objects.filter(
            client__office_id=self).filter(status_id=5).filter(type_id=3).aggregate(Sum('cash')).get('cash__sum')
        if depo is None:
            depo = 0
        if wd is None:
            wd = 0

        return depo - (2 * wd)

    @property
    def office_client_ammount_ftd_count(self):
        ftd_office_stats = Operation.objects.filter(
            client__office_id=self).filter(status_id=5).filter(type_id=4).count()
        if ftd_office_stats is None:
            ftd_office_stats = 0
        return ftd_office_stats

    @property
    def office_client_ammount_redepo_count(self):
        redepo_office_stats = Operation.objects.filter(
            client__office_id=self).filter(status_id=5).filter(type_id=2).count()
        if redepo_office_stats is None:
            redepo_office_stats = 0
        return redepo_office_stats

    @property
    def office_client_ammount_wd_count(self):
        wd_office_stats = Operation.objects.filter(
            client__office_id=self).filter(status_id=5).filter(type_id=3).count()
        if wd_office_stats is None:
            wd_office_stats = 0
        return wd_office_stats


class Menager(models.Model):
    def __str__(self):
        return self.name + ' ' + self.lastname

    name = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    phone = models.IntegerField()
    reg_time = models.DateField(auto_created=True)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)

    @property
    def m_employee_count(self):
        m_employee_count = Employee.objects.filter(manager_id=self).count()
        if m_employee_count is None: m_employee_count = 0
        return m_employee_count

    @property
    def m_ftd(self):
        m_ftd = Operation.objects.filter(who__manager_id=self).filter(type_id=4).filter(
            status_id=5).aggregate(Sum('cash')).get('cash__sum')
        if m_ftd is None: m_ftd = 0
        return m_ftd

    @property
    def m_depo(self):
        m_depo = Operation.objects.filter(who__manager_id=self).filter(status_id=5).filter(type_id=2).aggregate(
            Sum('cash')).get('cash__sum')
        if m_depo is None: m_depo = 0
        return m_depo

    @property
    def m_wd(self):
        m_wd = Operation.objects.filter(who__manager_id=self).filter(type_id=3).filter(status_id=5).aggregate(
            Sum('cash')).get('cash__sum')
        if m_wd is None:
            m_wd = 0
        return m_wd

    @property
    def m_all(self):
        m_depo = Operation.objects.filter(who__manager_id=self).filter(status_id=5).aggregate(Sum('cash')
                                                                                              ).get('cash__sum')
        m_wd = Operation.objects.filter(who__manager_id=self).filter(type_id=3).filter(status_id=5).aggregate(
            Sum('cash')).get('cash__sum')
        if m_depo is None: m_depo = 0
        if m_wd is None: m_wd = 0

        m_all = m_depo - (2 * m_wd)

        return m_all

    @property
    def m_ftd_count(self):
        m_ftd_count = Operation.objects.filter(who__manager_id=self).filter(type_id=4).filter(status_id=5).aggregate(
            Count('cash')).get('cash__count')

        return m_ftd_count

    @property
    def m_wd_count(self):
        m_wd_count = Operation.objects.filter(who__manager_id=self).filter(type_id=3).filter(status_id=5).aggregate(
            Count('cash')).get('cash__count')

        return m_wd_count

    @property
    def m_depo_count(self):
        m_depo_count = Operation.objects.filter(who__manager_id=self).filter(type_id=2).filter(status_id=5).aggregate(
            Count('cash')).get('cash__count')

        return m_depo_count


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
    reg_time = models.DateField(auto_now_add=True)
    office = models.ForeignKey(Office, on_delete=models.CASCADE, related_name='employe_office')
    manager = models.ForeignKey(Menager, on_delete=models.CASCADE)

    @property
    def e_ftd(self):
        emplo_ftd = Operation.objects.filter(who_id=self.id).filter(type_id=4).filter(
            status_id=5).aggregate(Sum('cash')).get('cash__sum')
        if emplo_ftd is None: emplo_ftd = 0
        return emplo_ftd

    @property
    def e_depo(self):
        emplo_depo = Operation.objects.filter(who_id=self.id).filter(status_id=5).filter(type_id=2).aggregate(
            Sum('cash')).get('cash__sum')
        if emplo_depo is None: emplo_depo = 0
        return emplo_depo

    @property
    def e_wd(self):
        emplo_wd = Operation.objects.filter(who_id=self.id).filter(type_id=3).filter(status_id=5).aggregate(
            Sum('cash')).get('cash__sum')
        if emplo_wd is None:
            emplo_wd = 0
        return emplo_wd

    @property
    def e_all(self):
        emplo_depo = Operation.objects.filter(who_id=self.id).filter(status_id=5).aggregate(Sum('cash')
                                                                                            ).get('cash__sum')
        emplo_wd = Operation.objects.filter(who_id=self.id).filter(type_id=3).filter(status_id=5).aggregate(
            Sum('cash')).get('cash__sum')
        if emplo_depo is None: emplo_depo = 0
        if emplo_wd is None: emplo_wd = 0

        emplo_all = emplo_depo - (2 * emplo_wd)

        return emplo_all

    @property
    def e_ftd_count(self):
        e_ftd_count = Operation.objects.filter(who_id=self.id).filter(type_id=4).filter(status_id=5).aggregate(
            Count('cash')).get('cash__count')

        return e_ftd_count

    @property
    def e_wd_count(self):
        e_wd_count = Operation.objects.filter(who_id=self.id).filter(type_id=3).filter(status_id=5).aggregate(
            Count('cash')).get('cash__count')

        return e_wd_count

    @property
    def e_depo_count(self):
        e_depo_count = Operation.objects.filter(who_id=self.id).filter(type_id=2).filter(status_id=5).aggregate(
            Count('cash')).get('cash__count')

        return e_depo_count


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
    office = models.ForeignKey(Office, on_delete=models.CASCADE, blank=True, null=True)
    active = models.BooleanField(default=False)

    @property
    def stats_ftd(self):
        cash_ftd = Operation.objects.filter(client_id=self.id).filter(type_id=4).filter(status_id=5).aggregate(
            Sum('cash')).get('cash__sum')
        if cash_ftd is None:
            cash_ftd = 0
        return cash_ftd

    @property
    def stats_depo(self):
        cash_depo = Operation.objects.filter(client_id=self.id).filter(type_id=2).filter(status_id=5).aggregate(
            Sum('cash')).get('cash__sum')
        if cash_depo is None:
            cash_depo = 0
        return cash_depo

    @property
    def stats_wd(self):

        cash_wd = Operation.objects.filter(client_id=self.id).filter(type_id=3).filter(status_id=5).aggregate(
            Sum('cash')).get('cash__sum')
        if cash_wd is None:
            cash_wd = 0
        return cash_wd

    @property
    def stats_all(self):
        cash_ba = Operation.objects.filter(client_id=self.id).filter(status_id=5).aggregate(
            Sum('cash')).get('cash__sum')
        cash_wd = Operation.objects.filter(client_id=self.id).filter(
            type_id=3).filter(
            status_id=5).aggregate(Sum('cash')).get('cash__sum')
        if cash_ba is None: cash_ba = 0
        if cash_wd is None:
            cash_wd = 0
        cash_balance = cash_ba - (2 * cash_wd)
        return cash_balance


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

    class Meta:
        verbose_name = 'Bank'
        verbose_name_plural = 'Banks'

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

    @property
    def bank_amount_depo(self):
        bank_depo = Operation.objects.filter(bank_id=self).filter(status_id=5).aggregate(Sum('cash')).get('cash__sum')
        bank_wd = Operation.objects.filter(bank_id=self).filter(
            status_id=5).filter(type_id=3).aggregate(Sum('cash')).get('cash__sum')
        if bank_wd is None:
            bank_wd = 0
        if bank_depo is None:
            bank_depo = 0

        return bank_depo - bank_wd

    @property
    def bank_amount_wd(self):
        bank_wd = Operation.objects.filter(bank_id=self).filter(
            status_id=5).filter(type_id=3).aggregate(Sum('cash')).get('cash__sum')
        if bank_wd is None:
            bank_wd = 0

        return bank_wd

    @property
    def bank_amount_operation_count(self):
        bank_count = Operation.objects.filter(bank_id=self).count()
        if bank_count is None:
            bank_count = 0

        return bank_count

    @property
    def bank_amount_bilans(self):
        bank_depo = Operation.objects.filter(bank_id=self).filter(status_id=5).aggregate(Sum('cash')).get('cash__sum')
        bank_wd = Operation.objects.filter(bank_id=self).filter(
            status_id=5).filter(type_id=3).aggregate(Sum('cash')).get('cash__sum')
        if bank_wd is None:
            bank_wd = 0
        if bank_depo is None:
            bank_depo = 0

        return bank_depo - (2 * bank_wd)


class Operation(models.Model):
    # def __str__(self):
    #     return self.client.name + ' ' + self.client.lastname + '  Cash: ' + str(self.cash)

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='operations')
    cash = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField(blank=True, null=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='operation_bank')
    type = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='operation_type')
    who = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='operation_status')

    class Meta:
        verbose_name = 'Operations'
        verbose_name_plural = 'Operations'
