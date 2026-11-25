from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .apps import UsersConfig
from .views import PaymentViewSet, UserCreateAPIView, UserPaymentHistoryView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"payments", PaymentViewSet)

urlpatterns = [
    path("my-payments/", UserPaymentHistoryView.as_view(), name="user-payment-history"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", UserCreateAPIView.as_view(), name="register"),
] + router.urls
