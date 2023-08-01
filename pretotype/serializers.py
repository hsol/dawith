from django.db import transaction
from rest_framework import serializers

from pretotype.models import Subscription


class SubscriptionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        exclude = ["reg_ts"]

    @transaction.atomic
    def create(self, validated_data):
        if subscription := Subscription.objects.filter(
            email=validated_data["email"],
            referer=validated_data["referer"],
        ).first():
            return subscription

        return super().create(validated_data)
