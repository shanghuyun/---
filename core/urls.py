# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, re_path, include  # add this
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from apps.home import views as home_views

urlpatterns = [
    #path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register

    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

else:
    urlpatterns +=(
        re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    )
    
handler404 = home_views.custom_404
handler403 = home_views.custom_403
handler500 = home_views.custom_500