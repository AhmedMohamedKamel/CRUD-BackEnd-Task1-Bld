from django.db import models

class Courses(models.Model):
    identification = models.CharField(max_length=3)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return 'ID: ' + self.identification + ' Course Name: ' + self.name