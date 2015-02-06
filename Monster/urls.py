from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from users import views
from users.api import UserResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Monster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'), # users 에 view.index 연결
    #url(r'^users/', include('users.urls')),
    url(r'^api/', include(v1_api.urls)),
    #url(r'^users/', include('users.urls', namespace="users")),
)
