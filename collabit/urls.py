from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'directory.views.index'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {"next_page": '/'}), 
    url(r'^signup/$', 'directory.views.signup'),
    url(r'^filter/$', 'directory.views.filter'),
    url(r'^register/$', 'directory.views.register'),
    url(r'^userProfile/(\d+)/$', 'directory.views.userProfile'),
    url(r'^submitGame/$', 'directory.views.submitGame'),
    # url(r'^collabit/', include('collabit.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
