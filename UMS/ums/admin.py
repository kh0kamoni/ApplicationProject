from django.contrib import admin
from .models import Department, Hall, Student, Teacher, Staff

# Register the models in the admin panel
admin.site.register(Department)
admin.site.register(Hall)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Staff)
