from django.conf import settings
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from users.models import Payment, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class UserPaymentHistorySerializer(ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ["id", "username", "payments"]
