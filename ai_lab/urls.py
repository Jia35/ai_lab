"""ai_lab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include

from django.conf.urls.static import static
from django.conf import settings

from monitor.views import home, aqm, upload_air, aquarium, test

urlpatterns = [
    re_path(r'^$', home, name='home'),
    path('admin/', admin.site.urls),

    path('aqm/', aqm, name='aqm'),
    path('aqm/pm', aqm, name='aqm_pm'),
    path('aqm/voc', aqm, name='aqm_voc'),
    path('aqm/mq9', aqm, name='aqm_mq9'),
    path('aqm/mq135', aqm, name='aqm_mq135'),
    path('aqm/th', aqm, name='aqm_th'),

    path('aquarium/', aquarium, name='aquarium'),
    path('test/', test, name='test'),

    path('upload_air/', upload_air, name='upload_air'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
