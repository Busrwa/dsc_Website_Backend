"""
URL configuration for dsc_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from blog.views import create_admin_user

urlpatterns = [
    path('secure-by/', admin.site.urls),
    path("create-admin/", lambda request: (create_admin_user(), HttpResponse("Admin oluşturuldu!"))[1]),

    path('api/blog/', include('blog.urls')),
    path('api/events/', include('events.urls')),
    path('api/sponsors/', include('sponsors.urls')),
    path('api/home/', include('home.urls')),
    path('api/team/', include('team.urls')),
    path('api/token/', obtain_auth_token),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
