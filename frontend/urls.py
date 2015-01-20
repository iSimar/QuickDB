from django.conf.urls import patterns, url

urlpatterns = patterns(
	'frontend.views',
	url(r'^$', 'login', name='login'),
	url(r'^signup/', 'signup', name='signup'),
)