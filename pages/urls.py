from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('taxrate/', views.test, name='taxrate'),
    path('<str:price>', views.calc, name='calc'),
]