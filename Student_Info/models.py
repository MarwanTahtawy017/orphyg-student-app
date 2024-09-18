from django.db import models

# Create your models here.


class GroupsList(models.Model):
    Group_Name = models.CharField(max_length = 400, primary_key = True, default = "Group name")

    def __str__(self):
        return self.Group_Name


class Student(models.Model):
    Full_Name = models.CharField(max_length = 400, primary_key = True)
    School = models.CharField(max_length = 400)
    Subject = models.CharField(max_length = 6)
    Grade = models.IntegerField()
    Email = models.EmailField(max_length = 400)
    Phone_Number = models.CharField(max_length = 11)
    Father_Number = models.CharField(max_length = 11)
    Mother_Number = models.CharField(max_length = 11)
    Group = models.ForeignKey(GroupsList, on_delete = models.CASCADE)

    def __str__(self):
        return self.Full_Name
