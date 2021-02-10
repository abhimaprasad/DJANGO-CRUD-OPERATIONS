
from django.urls import path,include
from.import views

urlpatterns = [
    path('',views.employeeform,name='employeeinsert'),
    path('<int:id>/',views.employeeform,name='employeeupdate'),
    path('delete/<int:id>/',views.employeeform,name='employeedelete'),
    path('list/',views.employeelist,name='employeelist'),
]
