from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from donations import urls as donations_urls


urlpatterns = [
    path('', TemplateView.as_view(template_name='pethome/home.html'), name='home'),
    path('pets/', include('pets.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    re_path(r'^', include(donations_urls)),


]