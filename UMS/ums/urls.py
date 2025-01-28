from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("student/signup/", views.student_signup, name="student_signup")
]