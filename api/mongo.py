import json

from backend.models import *
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

SUCCESS_INSERT = dict(result="Inserted", message="Insert Successful", success=1)
ERROR_INSERT_INVALID_FIELD_TYPE = dict(result="Error", message="one or more field type is invalid", success=0)
ERROR_INVALID_ACCESS_TOKEN = dict(result="Error", message="Invalid Access Token", success=0)

def getTable(access_token):
		try:
			table = Table.objects.get(access_token=access_token)
		except Table.DoesNotExist:
			table = None
		return table

def getTableFields(table):
	table_fields_with_types = {}
	table_fields = Table_Field.objects.filter(table=table).values('name', 'field_type')
	for table_field in table_fields:
		table_field_type = Table_Field_Type.objects.get(pk=table_field['field_type'])
		table_fields_with_types[table_field['name']] = str(table_field_type)
	return table_fields_with_types

class mongoCon:
	def __init__(self, port=27017):
		# print "init mongo connection"
		client = MongoClient('mongodb://localhost:'+str(port)+'/')

	def insert(self, access_token, insert_dict=dict()):
		table = getTable(access_token)
		if table is not None:
			final_dict = {}
			table_fields = getTableFields(table)
			try:
				for table_field in table_fields.keys():
					if(table_fields[table_field]=='integer'):
						if(table_field in insert_dict):
							final_dict[table_field] = int(insert_dict[table_field])
						else:
							final_dict[table_field] = int(0)
					elif(table_fields[table_field]=='string'):
						if(table_field in insert_dict):
							final_dict[table_field] = str(insert_dict[table_field])
						else:
							final_dict[table_field] = ''
				mongo_table = getattr(client.quickdb, access_token)
				mongo_table.insert(final_dict)
				return SUCCESS_INSERT
			except ValueError:
				return ERROR_INSERT_INVALID_FIELD_TYPE
		else:
			return ERROR_INVALID_ACCESS_TOKEN

	def get(self, access_token, get_dict=dict()):
		table = getTable(access_token)
		if table is not None:
			final_dict = {}
			table_fields = getTableFields(table)
			try:
				for get_dict_key in get_dict.keys():
					if(get_dict_key in table_fields):
						if(table_fields[get_dict_key]=='integer'):
							final_dict[get_dict_key] = int(get_dict[get_dict_key])
						elif(table_fields[get_dict_key]=='string'):
							final_dict[get_dict_key] = str(get_dict[get_dict_key])
				mongo_table = getattr(client.quickdb, access_token)
				print json.dumps(final_dict)
				rows = "["+', '.join([str(x) for x in mongo_table.find(final_dict, {'_id': False})])+"]"
				return rows
			except ValueError:
				return json.dumps(ERROR_INSERT_INVALID_FIELD_TYPE)
		else:
			return ERROR_INVALID_ACCESS_TOKEN