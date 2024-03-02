from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

import cores.authentication.urls  # type: ignore # noqa: I100
import cores.users.urls  # type: ignore # noqa: I100

API_PREFIX = 'api/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(API_PREFIX, include(cores.users.urls)),
    path(API_PREFIX, include(cores.authentication.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
