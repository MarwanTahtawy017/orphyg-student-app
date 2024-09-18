from django.urls import path
from . import views

urlpatterns = [
    path('sheet/<str:Group_Name>/', views.ShowHW),
    path('', views.SelectGroup),
]
