from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('tools_index/', views.tools_index, name='tools_index'),
    path('check_int_groove/', views.check_int_groove, name='check_int_groove'),
    path('check_int_turning/', views.check_int_turning, name='check_int_turning'),
    path('add_int_groove/', views.add_int_groove, name='add_int_groove'),
    path('add_int_turning/', views.add_int_turning, name='add_int_turning'),
    path('del_int_groove/', views.del_int_groove, name='del_int_groove'),
    path('del_int_turning/', views.del_int_turning, name='del_int_turning'),
]