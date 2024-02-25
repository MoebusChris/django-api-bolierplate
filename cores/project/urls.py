from django.contrib import admin
from django.urls import include, path

import cores.users.urls  # type: ignore # noqa: I100

API_PREFIX = 'api/'

urlpatterns = [path('admin/', admin.site.urls), path(API_PREFIX, include(cores.users.urls))]
