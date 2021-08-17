from django.urls import path
from tools import views


urlpatterns = [
    path('kanavka/', views.kanavka, name='kanavka'),
    path('rast/', views.rast),
    path('admin/', views.admin),
    path('akan/', views.akan),
    path('arast/', views.arast),
    path('dkan/', views.dkan),
    path('drast/', views.drast),
]
