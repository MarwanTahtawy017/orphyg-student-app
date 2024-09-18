from django.urls import path
from . import views


urlpatterns = [
    path('sheet/<str:Group_Name>/', views.ShowGrades, name='quizzes'),
    path('', views.SelectGroup),
]
