"""yoloapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path


# basic URL Configurations
from django.urls import include, path
# import routers
from rest_framework import routers

# import everything from views
from .views import *

from yoloapi import views 

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'geeks', GeeksViewSet)

# specify URL Path for rest_framework
urlpatterns = [
	path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('snippets/', views.snippet_list),

	path('api-auth/', include('rest_framework.urls')),
    path('image_upload', hotel_image_view, name='image_upload'),
	path('success', success, name='success'),
    path('index', index, name='image_upload'),


]

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,
						document_root=settings.MEDIA_ROOT)
