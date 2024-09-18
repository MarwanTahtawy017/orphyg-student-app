from django.shortcuts import render, get_list_or_404
from .models import HWSheet
from Student_Info.models import GroupsList

# Create your views here.

app_name = "Student_HW"


def ShowHW(request, Group_Name):
    Ordered_List = HWSheet.objects.order_by('-Date', 'This_Student')
    Student_in_Group = get_list_or_404(HWSheet, Student_Group = Group_Name)
    context = {'Ordered_List': Ordered_List,
               'Student_in_Group': Student_in_Group}
    return render(request, 'Student_HW/hwblog.html', context)


def SelectGroup(request):
    Groups = GroupsList.objects.all()
    context = {'Groups': Groups}
    return render(request, 'Student_HW/selectgroup.html', context)
