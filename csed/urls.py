from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('dbms/', views.dbms, name='detail'),
    path('da/', views.da, name='da'),
    path('ml/', views.ml, name='ml'),
    path('cd/', views.cd, name='cd'),
    path('daa/', views.daa, name='daa'),
]