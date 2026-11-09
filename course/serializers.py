from rest_framework import serializers
from course.models import Course, Lesson, Subscription
from course.validators import validate_no_external_links


class LessonSerializer(serializers.ModelSerializer):
    video_url = serializers.URLField(validators=[validate_no_external_links])
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = "__all__"

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Subscription.objects.filter(user=request.user, course=obj).exists()
        return False

class CourseDetailSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(many=True, read_only=True, source="lesson_set")
    number_of_lessons = serializers.SerializerMethodField()

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ("name", "description", "preview", "number_of_lessons", "lesson")
