from django.urls import path
from drf_spectacular.views import SpectacularRedocView, SpectacularAPIView

from pretotype.views import (
    LandingTemplateView,
    ContactTemplateView,
    SubscriptionCreateAPIView,
)

urlpatterns = [
    path("", LandingTemplateView.as_view()),
    path("contact", ContactTemplateView.as_view()),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("api/subscription", SubscriptionCreateAPIView.as_view()),
]
