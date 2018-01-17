"""MotionPictures URL Configuration

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
from django.views.generic.base import RedirectView

from django.contrib.auth import views as auth_views

from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap


from .settings import production
#from home.views import HomeView
#import photography.views 
from softwaredev.views import SoftwareView
from Webdev.views import WebdevView
from photography.views import gallary,AlbumDetail,AlbumSitemap
from home.views import photo_list
from contact_form.views import contact

sitemaps = {
        'photography':AlbumSitemap
}

urlpatterns = [
	
    url(r'^admin', admin.site.urls),
    url(r'^$',photo_list,name='photo_list'),
    url(r'^photography',gallary,name='gallary'),
    url(r'^(?P<slug>[-\w]+)$',AlbumDetail.as_view(),name='album'),
    url(r'^software/',SoftwareView.as_view(),name='SoftwareView'),
    url(r'^webdevelopement/',WebdevView.as_view(),name='WebdevView'),
    url(r'^contact/',contact, name='contact'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    name='django.contrib.sitemaps.views.sitemap'),
    
] + static(production.MEDIA_URL,document_root=production.MEDIA_ROOT)