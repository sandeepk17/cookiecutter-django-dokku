"""{{cookiecutter.app_name}} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from {{cookiecutter.app_name}} import settings
{%- if cookiecutter.use_rest_framework == "y" and cookiecutter.use_restframework_documentation == "y" %}
from rest_framework.documentation import include_docs_urls
{%- endif %}


{%- if cookiecutter.use_rest_framework == "y" and cookiecutter.use_auth_endpoints == "y" %}
api_v1_urlpatterns = [
    url(r'^auth/', include('{{cookiecutter.app_name}}.users.urls', namespace='users')),
]
{%- endif %}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    {%- if cookiecutter.use_rest_framework == "y" and cookiecutter.use_auth_endpoints == "y" %}
    url(r'^api/v1/', include(api_v1_urlpatterns, namespace='v1')),
    {%- elif cookiecutter.use_rest_framework == "n" and cookiecutter.use_auth_endpoints == "y" %}
    url(r'^accounts/', include('allauth.urls')),
    {%- endif %}
    {%- if cookiecutter.use_rest_framework == "y" and cookiecutter.use_restframework_documentation == "y" %}
    url(r'^docs/', include_docs_urls(title='{{cookiecutter.app_name}} API')),
    {%- endif %}
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
