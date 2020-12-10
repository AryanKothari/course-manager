
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('coursesapi', views.CourseView)


urlpatterns = [
    path("", views.index, name="index"),
    path("courses", views.courses, name="courses"),
    path("add", views.add, name="add"),
    path("courses/<str:course_title>/enrollcourse", views.enrollcourse, name="enroll_course"),
    path("courses/<str:course_title>/unenrollcourse", views.unenrollcourse, name="unenroll_course"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("", include(router.urls))
]
