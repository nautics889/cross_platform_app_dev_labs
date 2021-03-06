"""sandbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path, re_path

from sandbox.swagger import SchemaView

urlpatterns = [
    path(
        'admin/',
        admin.site.urls,
        name='admin'
    ),
    path(
        'o/',
        include('oauth2_provider.urls', namespace='oauth2_provider')
    ),
    re_path(
        r'^docs(?P<format>.json)/$',
        SchemaView.without_ui(cache_timeout=None),
        name='schema-json'
    ),
    path(
        'docs/',
        SchemaView.with_ui('swagger', cache_timeout=None),
        name='schema-swagger-ui'
    ),
    path(
        'users/',
        include('user_app.urls')
    ),
]
