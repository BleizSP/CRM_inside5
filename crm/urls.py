from django.urls import path
from crm import views

urlpatterns = [
    path('', views.index, name='index'),
    path('NewClient', views.new_client, name='new_client'),
    path('CompanySummary', views.company_summary, name='company_summary'),
    path('NewEmployees', views.new_employee, name='new_employee'),
    path('ClientList', views.client_list, name='client_list'),
    path('NewOperation', views.new_operation, name='new_operation'),
    path('NewBank', views.new_bank, name='new_bank'),
    path('EmployeesList', views.employees_list, name='employees_list'),
    path('NewOffice', views.new_office, name='new_office'),
]
