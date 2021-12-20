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
]
