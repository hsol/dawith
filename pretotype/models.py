from django.db import models


class Subscription(models.Model):
    email = models.EmailField(verbose_name="이메일")
    reg_ts = models.DateTimeField(verbose_name="생성일시", auto_now=True)

    class Meta:
        db_table = "pre_subscription"
        verbose_name = "사전구독"
