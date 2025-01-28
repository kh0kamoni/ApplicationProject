from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),

    # Student Urls
    path("student/signup/", views.student_signup, name="student_signup"),
    path("student/login/", views.student_login, name="student_login"),
    path("student/dashboard/", views.student_dashboard, name="student_dashboard"),
    path('student/logout/', views.student_logout, name='student_logout'),

    # Teacher Urls
    path("teacher/signup/", views.teacher_signup, name="teacher_signup"),
    path("teacher/login/", views.teacher_login, name="teacher_login"),
    path("teacher/dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
    path('teachers/logout/', views.teacher_logout, name='teacher_logout'),

    # Staff Urls
    path('staff/signup/', views.staff_signup, name='staff_signup'),
    path('staff/login/', views.staff_login, name='staff_login'),
    path('staff/dashboard/', views.staff_dashboard, name='staff_dashboard'),   
    path('staff/logout/', views.staff_logout, name='staff_logout'),
]