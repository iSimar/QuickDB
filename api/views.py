from django.http import HttpResponse
from backend.models import *
from django.views.decorators.csrf import csrf_exempt
import json
from pymongo import MongoClient

from mongo import mongoCon

table = mongoCon()

client = MongoClient('mongodb://localhost:27017/')

SUCCESS_INSERT = dict(result="Inserted", message="Insert Successful", success=1)
ERROR_INSERT = dict(result="Error", message="Must provide atleast one field", success=0)
ERROR_INVALID_ACCESS_TOKEN = dict(result="Error", message="Invalid Access Token", success=0)
ERROR_NO_ACCESS_TOKEN = dict(result="Error", message="No Access Token Provided", success=0)

@csrf_exempt
def v1_insert(request):
	access_token = request.POST.get('access_token', None)
	if access_token is not None:
		return HttpResponse(json.dumps(table.insert(access_token, request.POST)), content_type="application/json")
	else:
		return HttpResponse(json.dumps(ERROR_NO_ACCESS_TOKEN), content_type="application/json")

@csrf_exempt
def v1_get(request):
	access_token = request.POST.get('access_token', None)
	if access_token is not None:
		return HttpResponse(table.get(access_token, request.POST), content_type="application/json")
		# try:
		# 	table = Table.objects.get(access_token=access_token)
		# except Table.DoesNotExist:
		# 	table = None
		# if table:
		# 	filter_dict = {}
		# 	mongo_table = getattr(client.quickdb, access_token)
		# 	for post_variable in request.POST:
		# 		post_variable_value = request.POST.get(post_variable, None)
		# 		#cant use access_token, method, requrl as a fieldD
		# 		if post_variable not in ['access_token', 'method', 'requrl']:
		# 			try:
		# 			    post_variable_value = float(post_variable_value)
		# 			except ValueError:
		# 			    post_variable_value = post_variable_value

		# 			filter_dict[post_variable] = post_variable_value
		# 			print post_variable_value

		# 	all_objects = mongo_table.find(filter_dict, {'_id': False})
		# 	all_objects_string = "["+', '.join([str(x) for x in all_objects])+"]"
		# 	return HttpResponse(all_objects_string, content_type="application/json")
		# return HttpResponse(json.dumps(ERROR_INVALID_ACCESS_TOKEN), content_type="application/json")
	else:
		return HttpResponse(json.dumps(ERROR_NO_ACCESS_TOKEN), content_type="application/json")

