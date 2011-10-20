from django.conf.urls.defaults import patterns, include, url
from tastypie.api import Api
from myproject.api import PollResource, ChoiceResource
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(PollResource())
v1_api.register(ChoiceResource())

urlpatterns = patterns('',
    (r'^polls/', include('polls.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
)

