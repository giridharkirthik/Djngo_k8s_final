from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('m_p/', views.mainpage, name='mainpage'),
    path('add/', views.add, name='add'),
    path('UpDel/', views.UpDel, name='UpDel'),
    # path('att/', views.att, name='att'),
    path('alloc/', views.alloc, name='alloc'),
    path('menu/', views.menu, name='menu'),
    path('Schedule/', views.Schedule, name='Schedule'),
    path('showFlights/', views.showFlights, name='showFlights'),
    path('deleteFlight/<int:F>', views.deleteFlight, name='deleteFlight'),
    path('EmpDel/<int:sap>/', views.EmpDel, name='EmpDel'),
    path('editFlight/', views.EditFlights, name='EditFlights'),
    path('EditEmployees/<int:sap>', views.EditEmployees, name='EditEmployees'),
    path('UpdateEmployee/<int:sap>', views.UpdateEmployee, name='UpdateEmployee'),
    path('Group', views.Group, name='Group'),
    path('fail', views.fail, name='fail'),
]
