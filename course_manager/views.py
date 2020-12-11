from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Course
from .forms import NewCourseForm

from rest_framework import viewsets
from .serializers import CourseSerializer

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


def index(request):
    user = request.user
    courses = user.course.all()
    return render(request, "course_manager/index.html", {
        'user': user,
        'courses': courses,
        'courses_mon': courses.filter(day__contains="MON"),
        'courses_tue': courses.filter(day__contains="TUE"),
        'courses_wed': courses.filter(day__contains="WED"),
        'courses_thu': courses.filter(day__contains="THU"),
        'courses_fri': courses.filter(day__contains="FRI"),
    })

def add(request):
    if request.method == "POST":
        form = NewCourseForm(request.POST)
        if form.is_valid():
            course = Course()
            course.title = form.cleaned_data['title']
            course.professor = form.cleaned_data['professor']
            course.description = form.cleaned_data['description']
            course.subject = form.cleaned_data['subject']
            course.day = form.cleaned_data['day']
            course.start_time = form.cleaned_data['start_time']
            course.end_time = form.cleaned_data['end_time']
            course.save()
            return HttpResponseRedirect(reverse('courses'))
        else: 
            return render(request, "course_manager/add.html", {
                'form': NewCourseForm()
            })
    return render(request, "course_manager/add.html", {
        'form': NewCourseForm(),
    })

def courses(request):
    courses = Course.objects.all()
    user = User.objects.get(username=request.user)
    enrolled_courses = user.course.all().values_list('id', flat=True)

    
    return render(request, "course_manager/courses.html", {
        'courses': courses,
        'enrolled_courses': [int(s) for s in enrolled_courses],
    })

def enrollcourse(request, course_title):
    user = User.objects.get(username=request.user)
    course = Course.objects.get(title=course_title)
    user.course.add(course)
    return HttpResponseRedirect(reverse('courses'))

def unenrollcourse(request, course_title):
    user = User.objects.get(username=request.user)
    course = Course.objects.get(title=course_title)
    user.course.remove(course)
    return HttpResponseRedirect(reverse('courses'))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "course_manager/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "course_manager/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "course_manager/register.html", {
                "message": "Passwords must match.",
                'school_choices': ("apple", "banana", "cherry"),
            })
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "course_manager/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "course_manager/register.html", {
            'school_choices': ("apple", "banana", "cherry")
        })
