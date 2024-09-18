from django.shortcuts import render, get_list_or_404
from .models import QuizzesSheet
from Student_Info.models import GroupsList

# Create your views here.

app_name = "Student_Quizzes"


def ShowGrades(request, Group_Name):
    Ordered_List = QuizzesSheet.objects.order_by('-Day', 'This_Student')
    Student_in_Group = get_list_or_404(QuizzesSheet, Student_Group = Group_Name)
    context = {'Ordered_List': Ordered_List,
               'Student_in_Group': Student_in_Group}
    return render(request, 'Student_Quizzes/quizblog.html', context)


def SelectGroup(request):
    Groups = GroupsList.objects.all()
    context = {'Groups': Groups}
    return render(request, 'Student_Quizzes/selectgroup.html', context)
