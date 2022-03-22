from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=1024)
    start_date = models.DateField()


    def __str__(self):
        return self.title