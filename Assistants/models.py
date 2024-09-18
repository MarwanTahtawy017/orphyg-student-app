from django.db import models

# Create your models here.

class Assistant(models.Model):
    Name = models.CharField(max_length = 300)
    Subject = models.CharField(max_length = 400)
    Location = models.CharField(max_length = 300)
    Phone = models.CharField(max_length = 11)

    def __str__(self):
        return self.Name