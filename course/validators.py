import re
from urllib.parse import urlparse

from rest_framework.serializers import ValidationError

YOUTUBE_REGEX = re.compile(
    r"^(https?://)?(www.)?(m.)?(youtube.com|youtu.be)/.+$", re.IGNORECASE
)


def validate_no_external_links(value: str):
    """
    Валидатор для URL-полей.
    """
    if not value:
        return

    if not YOUTUBE_REGEX.match(value):
        raise ValidationError("Разрешены только ссылки на YouTube.")
