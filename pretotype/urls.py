from django.urls import path

from pretotype.views import LandingTemplateView

urlpatterns = [
    path("", LandingTemplateView.as_view()),
]
