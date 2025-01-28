from django.shortcuts import render, redirect
from django.contrib.auth import login
import datetime
from .forms import (
    StudentUserForm, StudentProfileForm, 
    TeacherUserForm, TeacherProfileForm,
    StaffUserForm, StaffProfileForm,
)

# Create your views here.
def landing(request):
    date = datetime.datetime.now()
    return render(request, "ums/landing.html", {
        "year": date.year
    })

# Student Signup View
def student_signup(request):
    if request.method == 'POST':
        user_form = StudentUserForm(request.POST)
        profile_form = StudentProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('student_dashboard')
    else:
        user_form = StudentUserForm()
        profile_form = StudentProfileForm()
    return render(request, 'ums/student_signup.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })