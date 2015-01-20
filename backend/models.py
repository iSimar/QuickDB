from django.db import models
from django.core.validators import URLValidator
from django.contrib.auth.models import User

class Table(models.Model):
	name = models.CharField(max_length=50)
	access_token = models.CharField(max_length=40)
	callback_url = models.TextField(validators=[URLValidator()])
	#---------------------------
	created = models.DateTimeField(auto_now_add=True)
	created.editable=True
	updated = models.DateTimeField(auto_now=True)
	updated.editable=True
	def __unicode__(self):
		return self.name

class Table_Field_Type(models.Model):
	name = models.CharField(max_length=20)
	#---------------------------
	created = models.DateTimeField(auto_now_add=True)
	created.editable=True
	updated = models.DateTimeField(auto_now=True)
	updated.editable=True
	def __unicode__(self):
		return self.name

class Table_Field(models.Model):
	name = models.CharField(max_length=60)
	field_type = models.ForeignKey(Table_Field_Type, null=True)
	table = models.ForeignKey(Table, null=True)
	#---------------------------
	created = models.DateTimeField(auto_now_add=True)
	created.editable=True
	updated = models.DateTimeField(auto_now=True)
	updated.editable=True
	def __unicode__(self):
		return self.table.name+" - "+self.name+"("+self.field_type.name+")"

class Circle(models.Model):
	user = models.ForeignKey(User, unique=True)
	table = models.ForeignKey(Table, null=True)
	#---------------------------
	created = models.DateTimeField(auto_now_add=True)
	created.editable=True
	updated = models.DateTimeField(auto_now=True)
	updated.editable=True
	def __unicode__(self):
		return self.user.username+" in "+self.table.name