"""djrenderfarm URL Configuration

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
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin, auth
from main_app import views
from django.contrib.auth import views as auth_views
from frontend import views as frontend_views

urlpatterns = [
    #url(r'^dashboard/', admin.site.urls),
    #url(r'^dashboard/login', auth.views.login),
    #url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    #url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$',  frontend_views.index),
    url(r'^register$',  frontend_views.register),
    url(r'^login/$',  frontend_views.login, name="frontend_login"),
    url(r'^contact$',  frontend_views.contact),
    url(r'^about_us$',  frontend_views.about_us),
    url(r'^project_monitoring$',  frontend_views.project_monitoring),
    url(r'^profile$',  frontend_views.profile),
    url(r'^services$',  frontend_views.services),
    url(r'^policy$',  frontend_views.policy),
    url(r'^statistic$',  frontend_views.under_construction),
    url(r'^news$',  frontend_views.news),
    url(r'^terms$',  frontend_views.terms),
    url(r'^logout$', auth_views.logout, {'next_page': 'frontend_login'}, name="frontend_logout"),
    url(r'^url_list',  views.urls),
    url(r'^dashboard/login', auth_views.login, {'template_name': 'dashboard/login.html'}, name='dashboard_login'),
    url(r'^dashboard/logout/$', auth_views.logout, {'next_page': 'dashboard_login'}, name="dashboard_logout"),
    url(r'^dashboard/', admin.site.urls),
    url(r'^dashboard/home', views.home),
    url(r'^dashboard/users/', include('users.urls')),
    url(r'^dashboard/projects/', include('projects.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
