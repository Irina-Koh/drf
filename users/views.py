from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from users.models import Payment, User
from users.serializers import (PaymentSerializer, UserPaymentHistorySerializer,
                               UserSerializer)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["user", "course", "lesson", "payment_date"]
    ordering_fields = ["payment_date", "amount"]
    ordering = ["-payment_date"]


class UserPaymentHistoryView(generics.RetrieveAPIView):
    serializer_class = UserPaymentHistorySerializer

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return settings.AUTH_USER_MODEL.objects.prefetch_related("payments")
