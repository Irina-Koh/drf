from datetime import timedelta

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from users.models import User


@shared_task
def send_course_update_email(user_email, course_title):
    subject = f"Обновление курса: {course_title}"
    message = f"В курсе «{course_title}» появились новые материалы."
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user_email],
        fail_silently=False,
    )


def block_inactive_users():
    """
    Блокирует пользователей, которые не заходили более 30 дней.
    Возвращает количество заблокированных.
    """
    cutoff = timezone.now() - timedelta(days=30)
    qs = User.objects.filter(
        last_login__lt=cutoff,
        is_active=True,
    )
    count = qs.update(is_active=False)
    return f"Blocked {count} user(s) inactive since {cutoff.isoformat()}"
