from django.db import models
from Student_Info.models import Student, GroupsList

# Create your models here.


class HWSheet(models.Model):
    Date = models.DateField()
    Done = models.BooleanField(default = False)
    Incomplete = models.BooleanField(default = False)
    Topic = models.CharField(max_length = 400)
    This_Student = models.ForeignKey(Student, on_delete = models.CASCADE)
    Student_Group = models.ForeignKey(GroupsList, on_delete = models.CASCADE)

    def __str__(self):
        if self.Done:
            Msg = self.This_Student.Full_Name + ": Done " + " " + str(self.Date)
        elif self.Incomplete:
            Msg = self.This_Student.Full_Name + ": Incomplete " + " " + str(self.Date)
        else:
            Msg = self.This_Student.Full_Name + ": Not done " + " " + str(self.Date)
        return Msg
