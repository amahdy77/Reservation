from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Reservation.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'expected_user.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),

)
