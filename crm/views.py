import datetime

from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
import sweetify

# Create your views here.
from crm.models import Employee, Bank, Status, Client, Operation, Office, Menager


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
    menago = Menager.objects.all()

    if request.method == "POST":
        nm = request.POST['firstname']
        ln = request.POST['lastname']
        ph = request.POST['telephone']
        em = request.POST['email']
        rk = request.POST['range']
        mn = request.POST['menago']

        data = Employee(
            name=nm, lastname=ln, phone=ph, email=em,
            rank=rk, office=office.get(menager=mn), manager_id=mn
        )
        data.save()
        sweetify.success(request, 'Gratulacje!',
                         text='Dobra robota, właśnie dodałeś: ' + nm + ' ' + ln + ' jako pracownika menadżera: ' + mn)

    return render(request, 'new_employees.html', {'office': office, 'menago': menago})


def new_client(request):
    employee = Employee.objects.all()
    office = Office.objects.all()

    banks = Bank.objects.filter(type='bank')
    posr = Bank.objects.filter(type='posrednik')
    crypto = Bank.objects.filter(type='crypto')

    if request.method == "POST":
        nm = request.POST['firstname']
        ln = request.POST['lastname']
        ph = request.POST['telephone']
        em = request.POST['email']
        ss = request.POST['salesman']
        ret = request.POST['retention']
        f_date = request.POST['ftd_date']
        f_bank = request.POST['ftd_bank']

        data = Client(
            name=nm, lastname=ln, phone=ph,
            email=em, salesman=Employee.objects.get(pk=ss), reg_time=f_date,
            retention=Employee.objects.get(pk=ret)
        )

        data.save()

        data = Operation(
            client_id=data.pk,
            cash=request.POST['cash'],
            bank=Bank.objects.get(pk=f_bank),
            date=request.POST['ftd_date'],
            status=Status.objects.get(pk=1),
            who=Employee.objects.get(pk=ss),
            type=Status.objects.get(pk=4)
        )

        data.save()

        sweetify.info(request, 'Gratulacje!',
                      text='Dobra robota, właśnie dodałeś klienta: ' + nm +
                           ' ' + ln + '  - Klient musi zostać zaakceptowany przez menagera.')

    return render(request, 'new_client.html', {'employee': employee, 'posr': posr, 'banks': banks, 'crypto': crypto,
                                               'office': office})


def new_operation(request):
    client = Client.objects.all()
    status = Status.objects.all()
    employee = Employee.objects.all()
    office = Office.objects.all()

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
            cash=cs, date=dd, type_id=tr,
            bank_id=ba, client_id=cl, status_id=1, who_id=ss
        )
        data.save()
        sweetify.info(request, 'Gratulacje!',
                      text='Dobra robota, właśnie dodałeś operacje, klient: ' + cl
                           + ' zrobił: ' + tr + ' na kwotę: ' + cs)

    return render(request, 'new_operation.html', {'client': client, 'status': status, 'employee': employee,
                                                  'posr': posr, 'banks': banks, 'crypto': crypto, 'office': office})


def client_list(request):
    employee = Employee.objects.all()
    transaction = Operation.objects.all()
    clients_list = Client.objects.all().filter(active=True)

    return render(request, 'client_list.html', {'clients_list': clients_list,
                                                'employee': employee,
                                                'transaction': transaction})


def employees_list(request):
    employee = Employee.objects.all()
    menago = Menager.objects.all()
    total_wd = Operation.objects.filter(status_id=5).filter(type_id=3).aggregate(Sum('cash')).get('cash__sum')
    total_depo = Operation.objects.filter(status_id=5).aggregate(Sum('cash')).get('cash__sum') - total_wd
    total_balance = Operation.objects.filter(status_id=5).aggregate(Sum('cash')).get('cash__sum') - (2 * total_wd)

    context = {
        'employee': employee,
        'total_depo': total_depo,
        'total_wd': total_wd,
        'total_balance': total_balance,
        'menago': menago,
    }

    return render(request, 'employee_list.html', context)


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


def office_list(request):
    operation = Operation.objects.all().filter(status_id=1)
    office = Office.objects.all()

    return render(request, 'office_list.html', {'office': office, 'operation': operation})


def pending_operations(req):
    operation = Operation.objects.all().filter(status_id=1)

    if req.method == 'POST':
        pending_accept = Operation.objects.get(pk=req.POST['accepted-id'])
        pending_accept.status_id = 5
        pending_accept.save(update_fields=['status_id'])

        sweetify.success(req, 'Gratulacje!',
                         text='Zatwierdzono! ' + pending_accept.client.name + ' ' + pending_accept.client.lastname)

    return render(req, 'pending_operations.html', {'operation': operation})


def new_menago(req):
    office = Office.objects.all()

    if req.method == 'POST':
        nm = req.POST['firstname']
        ln = req.POST['lastname']
        ph = req.POST['telephone']
        em = req.POST['email']
        of = req.POST['office']

        data = Menager(
            name=nm, lastname=ln, email=em, phone=ph, office_id=of, reg_time=datetime.date.today()
        )
        data.save()

        sweetify.success(req, 'Gratulacje!',
                         text='Dobra robota, właśnie dodałeś nowego menadżera: ' + nm + ' ' + ln)

    return render(req, 'new_menago.html', {'office': office})


def bank_list(req):
    operation = Operation.objects.all()
    bank = Bank.objects.all()

    contex = {
        'operation': operation,
        'bank': bank,
    }

    if req.method == 'POST':
        bank = Bank.objects.get(pk=req.POST['bank-id'])
        return redirect('bank', bank_id=bank.id)

    return render(req, 'bank_list.html', contex)


def bank(request, bank_id):
    bank = get_object_or_404(Bank, pk=bank_id)
    operation = Operation.objects.filter(bank_id=bank.id)

    context = {
        'bank': bank,
        'operation': operation,
    }

    return render(request, 'bank.html', context)


def client(request, client_id):
    Client.objects.all()

    if request.method == 'POST':
        client = Client.objects.get(pk=request.POST['client-id'])
        return redirect('client', client_id=client.id)

    context = {
        'client': client
    }

    return render(request, 'client.html', context)
