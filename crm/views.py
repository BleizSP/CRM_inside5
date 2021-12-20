import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
import sweetify

# Create your views here.
from crm.models import Employee, Bank, Status, Client, Operation


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
            reg_date=datetime.date.today(), status=True
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

    return render(request, 'new_employees.html')


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

    return render(request, 'new_operation.html', {'client': client, 'status': status, 'employee': employee,
                                                  'posr': posr, 'banks': banks, 'crypto': crypto})


def client_list(request):
    employee = Employee.objects.all()
    clients_list = Client.objects.all()
    operation = Operation.objects.all()

    return render(request, 'client_list.html', {'clients_list': clients_list,
                                                'employee': employee, 'operation': operation})
