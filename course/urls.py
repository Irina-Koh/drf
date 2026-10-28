from django.urls import include, path
from rest_framework.routers import SimpleRouter

from course.views import (CourseViewSet, LessonCreateApiView,
                          LessonDestroyApiView, LessonListApiView,
                          LessonRetrieveApiView, LessonUpdateApiView)

app_name = "courses"

router = SimpleRouter()

router.register("courses", CourseViewSet, basename="course")

lesson_urls = [
    path("lessons/", LessonListApiView.as_view(), name="lesson_list"),
    path("lessons/create/", LessonCreateApiView.as_view(), name="lesson_create"),
    path("lessons/int:pk/", LessonRetrieveApiView.as_view(), name="lesson_retrieve"),
    path("lessons/int:pk/update/", LessonUpdateApiView.as_view(), name="lesson_update"),
    path(
        "lessons/int:pk/delete/", LessonDestroyApiView.as_view(), name="lesson_delete"
    ),
]

urlpatterns = router.urls + lesson_urls
