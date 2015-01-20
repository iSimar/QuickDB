from django.conf.urls import patterns, url

urlpatterns = patterns(
	'api.views',
	url(r'^v1/insert', 'v1_insert', name='v1_insert'),
	url(r'^v1/get', 'v1_get', name='v1_get'),
	# get_one
	# modify
)