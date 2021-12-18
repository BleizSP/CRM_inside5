from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Employees.models import Employees
from Clients.models import Client
from Operation.models import Operation, Status
import sweetify


# Create your views here.
def index(request):
    return render(request, 'home.html')


def new_client(request):
    employees = Employees.objects.all()

    if request.method == "POST":
        nm = request.POST['firstname']
        ln = request.POST['lastname']
        ph = request.POST['telephone']
        em = request.POST['email']
        ss = request.POST['salesman']
        f_date = request.POST['ftd_date']
        f_bank = request.POST['ftd_bank']

        data = Client(
            client_name=nm, client_lastname=ln, client_phone=ph,
            client_email=em, client_salesman=Employees.objects.get(pk=ss), client_reg_time=f_date,
            client_bank=f_bank
        )

        data.save()

        data = Operation(
            operation_client_id=data.pk,
            operation_client_cash=request.POST['cash'],
            operation_bank=request.POST['ftd_bank'],
            operation_date=request.POST['ftd_date'],
            operation_status=Status.objects.get(pk=1),
        )

        data.save()

        sweetify.info(request, 'Gratulacje!',
                      text='Dobra robota, właśnie dodałeś klienta: ' + nm + ' ' + ln + '  - Klient musi zostać zaakceptowany przez menagera.')

    return render(request, 'new_client.html', {'employees': employees})


def company_summary(request):
    return render(request, 'company_summary.html')


def new_employees(request):
    if request.method == "POST":
        nm = request.POST['firstname']
        ln = request.POST['lastname']
        ph = request.POST['telephone']
        em = request.POST['email']
        rk = request.POST['range']
        of = request.POST['office']

        data = Employees(
            employees_name=nm, employees_lastname=ln, employees_phone=ph, employees_email=em,
            employees_rank=rk, employees_group=of
        )
        data.save()
        sweetify.success(request, 'Gratulacje!',
                         text='Dobra robota, właśnie dodałeś: ' + nm + ' ' + ln + ' jako pracownika grupy: ' + of)

    return render(request, 'new_employees.html')


def client_list(request):
    employees = Employees.objects.all()
    clients_list = Client.objects.all()

    return render(request, 'client_list.html', {'clients_list': clients_list,
                                                'employees': employees})
