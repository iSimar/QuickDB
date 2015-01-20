from django.shortcuts import render_to_response
from django.http import HttpResponse

def login(request):
	return render_to_response('frontend/index.html')