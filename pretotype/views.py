# Create your views here.
from django.views.generic import TemplateView
from rest_framework.generics import CreateAPIView

from pretotype.models import Subscription
from pretotype.serializers import SubscriptionModelSerializer


class LandingTemplateView(TemplateView):
    template_name = "pretotype/landing.jinja2"


class ContactTemplateView(TemplateView):
    template_name = "pretotype/contact.jinja2"


class SubscriptionCreateAPIView(CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionModelSerializer
