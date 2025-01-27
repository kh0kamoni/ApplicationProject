from django.db import models

# Department table
class Department(models.Model):
    dept_code = models.CharField(max_length=8)
    dept_name = models.CharField(max_length=64)

    def __str__(self):
        return self.dept_name

# Hall table
class Hall(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

# Student table
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    dept_name = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    roll = models.IntegerField()
    reg = models.IntegerField()
    session = models.CharField(max_length=64)
    hall = models.ForeignKey(Hall, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

# Teacher table (without extending User)
class Teacher(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    date_of_joining = models.DateField()

    def __str__(self):
        return self.name

# Staff table (without extending User)
class Staff(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    hall = models.ForeignKey(Hall, on_delete=models.SET_NULL, null=True)
    position = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    

# Course table
class Course(models.Model):
    # List for semester choices (1 and 2)
    SEMESTER_CHOICES = [
        (1, 'Semester 1'),
        (2, 'Semester 2'),
    ]

    # List for year choices (1 to 4)
    YEAR_CHOICES = [
        (1, 'Year 1'),
        (2, 'Year 2'),
        (3, 'Year 3'),
        (4, 'Year 4'),
    ]

    course_code = models.CharField(max_length=64)
    course_name = models.CharField(max_length=64)
    semester = models.IntegerField(choices=SEMESTER_CHOICES)
    year = models.IntegerField(choices=YEAR_CHOICES)
    dept_name = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.course_name