from .base import *

CSRF_TRUSTED_ORIGINS = ["http://dawith.us"]
DEBUG = False
MIDDLEWARE.append("django.middleware.cache.FetchFromCacheMiddleware")
