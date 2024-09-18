from django.db import models
from Student_Info.models import Student, GroupsList

# Create your models here.


class AttendanceSheet(models.Model):

    Date = models.DateField()
    Attended = models.BooleanField(default = False)
    This_Student = models.ForeignKey(Student, on_delete = models.CASCADE)
    Student_Group = models.ForeignKey(GroupsList, on_delete = models.CASCADE)

    def __str__(self):
        if self.Attended:
            Msg = self.This_Student.Full_Name + ": Attended " + str(self.Date)
        else:
            Msg = self.This_Student.Full_Name + ": Did not attend " + str(self.Date)
        return Msg
