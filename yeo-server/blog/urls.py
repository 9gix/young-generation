from django.conf.urls.defaults import *
from blog.views import *

urlpatterns = patterns('',
    (r'^$',blog),
)
