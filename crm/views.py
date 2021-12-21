import datetime

from django.shortcuts import render
import sweetify

# Create your views here.
from crm import models
from crm.models import Employee, Bank, Status, Client, Operation, Office


def new_bank(request):
    if request.method == 'POST':
        nn = request.POST['name']
        tp = request.POST['meth']
        ib = request.POST['iban']
        sw = request.POST['swift']
        co = request.POST['country']
        ad = request.POST['adress']
        ac = request.POST['account']
        wl = request.POST['wallet']

        data = Bank(
            name=nn, type=tp, iban=ib, wallet=wl, owner=ac, swift=sw, country=co, adres=ad,
            reg_date=datetime.date.today(), active=True
        )

        data.save()

        sweetify.info(request, 'Gratulacje!',
                      text='Dobra robota, właśnie dodałeś nową metode płatności: ' + nn)

    return render(request, 'new_bank.html')


def index(request):
    return render(request, 'home.html')


def company_summary(request):
    return render(request, 'company_summary.html')


def new_employee(request):
    office = Office.objects.all()

    if request.method == "POST":
        nm = request.POST['firstname']
        ln = request.POST['lastname']
        ph = request.POST['telephone']
        em = request.POST['email']
        rk = request.POST['range']
        of = request.POST['office']

        data = Employee(
            name=nm, lastname=ln, phone=ph, email=em,
            rank=rk, group=of
        )
        data.save()
        sweetify.success(request, 'Gratulacje!',
                         text='Dobra robota, właśnie dodałeś: ' + nm + ' ' + ln + ' jako pracownika grupy: ' + of)

    return render(request, 'new_employees.html', {'office': office})


def new_client(request):
    employee = Employee.objects.all()

    banks = Bank.objects.filter(type='bank')
    posr = Bank.objects.filter(type='posrednik')
    crypto = Bank.objects.filter(type='crypto')

    if request.method == "POST":
        nm = request.POST['firstname']
        ln = request.POST['lastname']
        ph = request.POST['telephone']
        em = request.POST['email']
        ss = request.POST['salesman']
        f_date = request.POST['ftd_date']
        f_bank = request.POST['ftd_bank']

        data = Client(
            name=nm, lastname=ln, phone=ph,
            email=em, salesman=Employee.objects.get(pk=ss), reg_time=f_date,
            retention=Employee.objects.get(pk=ss)
        )

        data.save()

        data = Operation(
            client_id=data.pk,
            cash=request.POST['cash'],
            bank=Bank.objects.get(pk=f_bank),
            date=request.POST['ftd_date'],
            status=Status.objects.get(pk=1),
            who=Employee.objects.get(pk=ss)
        )

        data.save()

        sweetify.info(request, 'Gratulacje!',
                      text='Dobra robota, właśnie dodałeś klienta: ' + nm + ' ' + ln + '  - Klient musi zostać zaakceptowany przez menagera.')

    return render(request, 'new_client.html', {'employee': employee, 'posr': posr, 'banks': banks, 'crypto': crypto})


def new_operation(request):
    client = Client.objects.all()
    status = Status.objects.all()
    employee = Employee.objects.all()

    banks = Bank.objects.filter(type='bank')
    posr = Bank.objects.filter(type='posrednik')
    crypto = Bank.objects.filter(type='crypto')

    if request.method == 'POST':
        cl = request.POST['client']
        ss = request.POST['salesman']
        tr = request.POST['trans']
        cs = request.POST['cash']
        dd = request.POST['date']
        ba = request.POST['bank']

        data = Operation(
            cash=cs, date=dd, type=tr,
            bank_id=ba, client_id=cl, status_id=4, who_id=ss
        )
        data.save()
        sweetify.info(request, 'Gratulacje!',
                      text='Dobra robota, właśnie dodałeś operacje, klient: ' + cl
                           + ' zrobił: ' + tr + ' na kwotę: ' + cs)

    return render(request, 'new_operation.html', {'client': client, 'status': status, 'employee': employee,
                                                  'posr': posr, 'banks': banks, 'crypto': crypto})


def client_list(request):
    employee = Employee.objects.all()
    clients_list = Client.objects.all()

    return render(request, 'client_list.html', {'clients_list': clients_list,
                                                'employee': employee})


def employees_list(request):
    employee = Employee.objects.all()

    return render(request, 'employee_list.html', {'employee': employee})


def new_office(request):
    if request.method == 'POST':
        nm = request.POST['office_name']
        ln = request.POST['country']

        data = Office(
            name=nm, country=ln
        )
        data.save()
        sweetify.success(request, 'Gratulacje!',
                         text='Dobra robota, właśnie dodałeś nowe biuro: ' + nm + ' z kraju: ' + ln)

    return render(request, 'new_office.html')
