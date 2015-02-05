from django.conf.urls import patterns, include, url
from django.contrib import admin
from users import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Monster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'), # users 에 view.index 연결
    url(r'^users/', include('users.urls')),
    #url(r'^users/', include('users.urls', namespace="users")),
)
