from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)), # url that sets admin page
	url(r'^$', 'joins.views.home', name='home'), # lwc folder then views script then home module
	url(r'^fb/', 'joins.views.fb', name='fb'), 
	url(r'^(?P<ref_id>.*)$', 'joins.views.share', name='share'), 
	url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'login_app.views.home', name='home'),
    url(r'^members/', 'login_app.views.members', name='members'),
    url(r'^logout/$', 'login_app.views.logout', name='logout'),
	#url(r'^home2/$', 'joins.views.home2', name='home'),
	# first argument is url with request being sent to lwc.views.home, module will return 
    # url(r'^blog/', include('blog.urls')),
	# url(r'^home2/$', 'lwc.views.home2', name='home'),
	
    
)
