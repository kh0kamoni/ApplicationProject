from django.db import models

# Create your models here.
class Department(models.Model):
    dept_code = models.CharField(max_length=8)
    dept_name = models.CharField(max_length=64)

    def __str__(self):
        return self.dept_name
    

class Student