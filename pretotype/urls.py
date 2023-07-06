from django.urls import path

from pretotype.views import LandingTemplateView, ContactTemplateView

urlpatterns = [
    path("", LandingTemplateView.as_view()),
    path("contact", ContactTemplateView.as_view()),
]
