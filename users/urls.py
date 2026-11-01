from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PaymentViewSet, UserPaymentHistoryView

router = DefaultRouter()
router.register(r"payments", PaymentViewSet)

urlpatterns = [
    path("my-payments/", UserPaymentHistoryView.as_view(), name="user-payment-history"),
] + router.urls
