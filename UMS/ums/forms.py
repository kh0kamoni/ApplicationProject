from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student, Teacher, Staff, Department, Hall, Course

# Student Forms
class StudentUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "dept_name", "roll", "reg", "session", "hall"]


# Teachers Forms
class TeacherUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'designation', 'course_teaches', 'department', 'date_of_joining']

# Staff Forms
class StaffUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class StaffProfileForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'position']
