from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	
	url(r'u/(?P<uid>\d+)/$', 'workouts_app.views.userhome'),

    url(r'^$', 'workouts_app.views.home', name='home'),
	url(r'u/(?P<uid>\d+)/random/$', 'workouts_app.views.random_workout'),
		
    url(r'u/(?P<uid>\d+)/(?P<wkout_num>\d+)/$', 'workouts_app.views.wkdetail'),
	
	url(r'u/(?P<uid>\d+)/addworkout/$', 'workouts_app.views.addworkout'),	
	# Examples:
    # url(r'^workout_project/', include('workout_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
