from .base import *

CSRF_TRUSTED_ORIGINS = ["http://dawith.us", "https://dawith.us"]
DEBUG = False
MIDDLEWARE.append("django.middleware.cache.FetchFromCacheMiddleware")

SECURE_SSL_REDIRECT = True
SECURE_SSL_HOST = "dawith.us"
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
