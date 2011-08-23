from django.conf.urls.defaults import *
from django.contrib import admin
from blog.models import PostsSitemap
from minicms.models import PagesSitemap

admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

sitemaps = {
    'posts': PostsSitemap,
    'pages': PagesSitemap,
}

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/',include('blog.urls')),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps}),
    (r'^robots\.txt$', 'robots.views.robots'),
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'index.html'}),
)
