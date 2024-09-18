from django.urls import path
from . import views


urlpatterns = [
    path('sheet/<str:Group_Name>/', views.ShowAtt, name = 'attendance'),
    path('', views.SelectGroup),
    path('record/', views.RecordAtt)
]
