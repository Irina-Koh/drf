from django.db import models


class Course(models.Model):
    name = models.CharField(
        max_length=500,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание курса",
        help_text="Введите описание курса",
    )
    preview = models.ImageField(
        upload_to="course/previews_course",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите превью",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        help_text="Выберете курс",
    )
    name = models.CharField(
        max_length=500,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание урока",
        help_text="Введите описание урока",
    )
    preview = models.ImageField(
        upload_to="course/previews_lesson",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите превью",
    )
    video_url = models.URLField(
        verbose_name="Ссылка на видео", help_text="Укажите ссылку на видео урока"
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
