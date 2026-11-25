from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from course.models import Course, Lesson
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="arina2009.91@mail.ru")
        self.course = Course.objects.create(
            name="Python", description="I love Python", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            name="Python", course=self.course, owner=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        url = reverse("course:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.course.name)

    def test_course_create(self):
        url = reverse("course:course-list")
        data = {"name": "django"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.all().count(), 2)

    def test_course_update(self):
        url = reverse("course:course-detail", args=(self.course.pk,))
        data = {"name": "Postgre"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Postgre")

    def test_course_delete(self):
        url = reverse("course:course-detail", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.all().count(), 0)

    def test_course_list(self):
        url = reverse("course:course-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.course.pk,
                    "is_subscribed": False,
                    "name": self.course.name,
                    "description": self.course.description,
                    "preview": None,
                    "owner": self.user.pk,
                }
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="arina2009.91@mail.ru", password="password"
        )
        self.course = Course.objects.create(
            name="Python", description="I love Python", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            name="Python",
            course=self.course,
            video_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("course:lesson_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)

    def test_lesson_create(self):
        url = reverse("course:lesson_create")
        data = {
            "course": self.course.id,
            "name": "django",
            "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("course:lesson_update", args=(self.lesson.pk,))
        data = {
            "course": self.course.id,
            "name": "django2",
            "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "django2")

    def test_lesson_delete(self):
        url = reverse("course:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("course:lesson_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "video_url": self.lesson.video_url,
                    "name": self.lesson.name,
                    "description": None,
                    "preview": None,
                    "course": self.course.pk,
                    "owner": self.user.pk,
                }
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
