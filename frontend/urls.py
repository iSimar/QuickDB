from django.conf.urls import patterns, url

urlpatterns = patterns(
	'frontend.views',
	url(r'^', 'login', name='login'),
)