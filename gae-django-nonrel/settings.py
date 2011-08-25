# -*- coding: utf-8 -*-

# The following takes care of auto-configuring the database. You might want to
# modify this to match your environment (i.e., without fallbacks).

from djangoappengine.settings_base import *

import os

# Activate django-dbindexer for the default database
DATABASES['native'] = DATABASES['default']
DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}
AUTOLOAD_SITECONF = 'dbindexes'

SITE_NAME = 'Young Generation'
SITE_DESCRIPTION = 'Young Generation'
SITE_COPYRIGHT = 'young-gene.appspot.com'
DISQUS_SHORTNAME = 'young-gene'
GOOGLE_ANALYTICS_ID = 'UA-25348821-1'
# Get the ID from the CSE "Basics" control panel ("Search engine unique ID")
GOOGLE_CUSTOM_SEARCH_ID = '005997832323097011877:jokucbrqnt0'
# Set RT username for retweet buttons
TWITTER_USERNAME = 'ye0eugene0ey'
# In order to always have uniform URLs in retweets and FeedBurner we redirect
# any access to URLs that are not in ALLOWED_DOMAINS to the first allowed
# domain. You can have additional domains for testing.
ALLOWED_DOMAINS = ()

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.sitemaps',
    'urlrouter',
    'minicms',
    'blog',
    'disqus',
    'djangotoolbox',
    'google_analytics',
    'google_cse',
    'mediagenerator',
    'robots',
    'simplesocial',
    'redirects',
    'autoload',
    'dbindexer',
    'djangoappengine',
)
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

REST_BACKENDS = (
    'minicms.markup_highlight',
    'blog.markup_posts',
)

MIDDLEWARE_CLASSES = (
    # This loads the index definitions, so it has to come first
    'autoload.middleware.AutoloadMiddleware',

    'mediagenerator.middleware.MediaMiddleware',

    'django.middleware.common.CommonMiddleware',
    'djangotoolbox.middleware.RedirectMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'urlrouter.middleware.URLRouterFallbackMiddleware',
)

URL_ROUTE_HANDLERS = (
    'minicms.urlroutes.PageRoutes',
    'blog.urlroutes.BlogRoutes',
    'blog.urlroutes.BlogPostRoutes',
    'redirects.urlroutes.RedirectRoutes',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'minicms.context_processors.cms',
)

USE_I18N = False

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

MEDIA_BUNDLES = (
    ('main.css',
        'css/style.css'
    ),
)
#
#ROOT_MEDIA_FILTERS = {
#    'js': 'mediagenerator.filters.closure.Closure',
#    'css': 'mediagenerator.filters.yuicompressor.YUICompressor',
#}
#
#CLOSURE_COMPILER_PATH = os.path.join(os.path.dirname(__file__),
#                                     '.webutils', 'compiler.jar')
#
#YUICOMPRESSOR_PATH = os.path.join(os.path.dirname(__file__),
#                                  '.webutils', 'yuicompressor.jar')

MEDIA_DEV_MODE = DEBUG
DEV_MEDIA_URL = '/devmedia/'
PRODUCTION_MEDIA_URL = '/media/'

GLOBAL_MEDIA_DIRS = (
    os.path.join(os.path.dirname(__file__), 'static'),
)

ADMIN_MEDIA_PREFIX = '/media/admin/'

ROOT_URLCONF = 'urls'

NON_REDIRECTED_PATHS = ('/admin/',)

try:
    from settings_local import *
except ImportError:
    pass
