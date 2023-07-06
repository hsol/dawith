# Create your views here.
from django.views.generic import TemplateView


class LandingTemplateView(TemplateView):
    template_name = "pretotype/landing.jinja2"


class ContactTemplateView(TemplateView):
    template_name = "pretotype/contact.jinja2"
