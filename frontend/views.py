from django.shortcuts import render_to_response
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
	emailInput = request.POST.get('emailInput', None)
	passwordInput = request.POST.get('passwordInput', None)
	if not emailInput is None:
		if not passwordInput is None:
			user = authenticate(username=emailInput, password=passwordInput)
			if user is not None:
				login(request, user)
				#render to response -> dashboard
			else:
				return render_to_response('frontend/index.html',
										  dict(error=True, username=emailInput))
	return render_to_response('frontend/index.html')

@csrf_exempt
def signup(request):
	emailInput = request.POST.get('emailInput', None)
	passwordInput = request.POST.get('passwordInput', None)
	confirmPasswordInput = request.POST.get('confirmPasswordInput', None)
	if not emailInput is None:
		if not passwordInput is None:
			if confirmPasswordInput == passwordInput:
				if User.objects.filter(username=emailInput).count():
					return render_to_response('frontend/signup.html', dict(usernameExists=True, username=emailInput))
				else:
					user = User.objects.create_user(emailInput, emailInput, passwordInput)
					return render_to_response('frontend/index.html', dict(userCreated=True))
			else:
				return render_to_response('frontend/signup.html', dict(passwordDontMatch=True))
	return render_to_response('frontend/signup.html')