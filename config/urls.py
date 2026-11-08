from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("course/", include("course.urls", namespace="course")),
    path("users/", include("users.urls", namespace="users")),
]
