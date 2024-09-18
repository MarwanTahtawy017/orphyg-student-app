from django.shortcuts import render, get_list_or_404
from .models import AttendanceSheet
from Student_Info.models import GroupsList, Student
from .forms import RecordAttForm
from datetime import date

# Create your views here.

app_name = "Student_Attendance"


def ShowAtt(request, Group_Name):
    Ordered_List = AttendanceSheet.objects.order_by('-Date', 'This_Student')
    Student_in_Group = get_list_or_404(AttendanceSheet, Student_Group = Group_Name)
    context = {'Ordered_List': Ordered_List,
               'Student_in_Group': Student_in_Group}
    return render(request, 'Student_Attendance/attblog.html', context)


def SelectGroup(request):
    Groups = GroupsList.objects.all()
    context = {'Groups': Groups}
    return render(request, 'Student_Attendance/selectgroup.html', context)


def RecordAtt(request):
    if request.method == 'POST':
        form = RecordAttForm(request.POST)
        if form.is_valid():
            Student_List = Student.objects.order_by('Full_Name')
            StudentFullName = form.cleaned_data.get('StudentFullName')
            for i in Student_List:
                if StudentFullName == i.Full_Name:
                    ThisGroup = GroupsList(Group_Name = i.Group)
                    AttEntry = AttendanceSheet(Date = date.today(), Attended = True, This_Student = i,
                                               Student_Group = ThisGroup)
                    AttEntry.save()
                    break
    else:
        form = RecordAttForm()
    return render(request, 'Student_Attendance/recordatt.html', {'form': form})
