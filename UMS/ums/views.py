from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Student, Teacher, Staff
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


# Teacher Signup
def teacher_signup(request):
    if request.method == "POST":
        user_form = TeacherUserForm(request.POST)
        profile_form = TeacherProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect("teacher_dashboard")
    else:
        user_form = TeacherProfileForm()
        profile_form = TeacherProfileForm()
    return render(request, "ums/teacher_signup.html", {
        "user_form": user_form,
        "profile_form": profile_form,
    })

def staff_signup(request):
    if request.method == 'POST':
        user_form = StaffUserForm(request.POST)
        profile_form = StaffProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('staff_dashboard')
    else:
        user_form = StaffUserForm()
        profile_form = StaffProfileForm()
    return render(request, 'ums/staff_signup.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })





# Student Login View
def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and hasattr(user, 'student'):
            login(request, user)
            return redirect('student_dashboard')
        else:
            return render(request, 'ums/student_login.html', {'error': 'Invalid credentials or not a student account.'})
    return render(request, 'ums/student_login.html')

# Teacher Login View
def teacher_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and hasattr(user, 'teacher'):
            login(request, user)
            return redirect('teacher_dashboard')
        else:
            return render(request, 'ums/teacher_login.html', {'error': 'Invalid credentials or not a teacher account.'})
    return render(request, 'ums/teacher_login.html')

# Staff Login View
def staff_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and hasattr(user, 'staff'):
            login(request, user)
            return redirect('staff_dashboard')
        else:
            return render(request, 'staff_login.html', {'error': 'Invalid credentials or not a staff account.'})
    return render(request, 'ums/staff_login.html')

# Dashboard Views
@login_required
def student_dashboard(request):
    return render(request, 'ums/student_dashboard.html')

@login_required
def teacher_dashboard(request):
    return render(request, 'ums/teacher_dashboard.html')

@login_required
def staff_dashboard(request):
    return render(request, 'ums/staff_dashboard.html')









def student_logout(request):
    logout(request)
    return redirect('student_login')

def teacher_logout(request):
    logout(request)
    return redirect('teacher_login')

def staff_logout(request):
    logout(request)
    return redirect('staff_login')