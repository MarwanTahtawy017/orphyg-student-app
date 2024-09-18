from django.db import models
from Student_Info.models import Student, GroupsList

# Create your models here.


class QuizzesSheet(models.Model):

    Day = models.DateField()
    Topic = models.CharField(max_length = 400)
    Student_Mark = models.IntegerField()
    Full_Mark = models.IntegerField()

    @property
    def CalculateGrade(self):

        Percentage = (self.Student_Mark / self.Full_Mark) * 100

        if Percentage >= 78:
            GradeChar = "A*"
        elif 65 <= Percentage < 78:
            GradeChar = "A"
        elif 55 <= Percentage < 65:
            GradeChar = "B"
        elif 45 <= Percentage < 55:
            GradeChar = "C"
        elif 35 <= Percentage < 45:
            GradeChar = "D"
        else:
            GradeChar = "U"

        return GradeChar

    Quiz_Grade = CalculateGrade
    This_Student = models.ForeignKey(Student, on_delete = models.CASCADE)
    Student_Group = models.ForeignKey(GroupsList, on_delete = models.CASCADE)

    def __str__(self):
        return self.This_Student.Full_Name + ": " + self.Quiz_Grade + " " + self.Topic
