"""AndersonMcGortyLabDB_Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include("website.urls")),
    path("members/", include('django.contrib.auth.urls')),
    path("members/", include("members.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.META_URL, document_root=settings.META_ROOT) + static(settings.ADDITION_URL, document_root=settings.ADDITION_ROOT) + static(settings.BARCODE_URL, document_root=settings.BARCODE_ROOT) + static(settings.DISPLAY_URL, document_root=settings.DISPLAY_ROOT)
