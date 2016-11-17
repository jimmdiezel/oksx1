import uuid
from django.db import models

# Create your models here.


class user(models.Model):
	first_name = models.CharField('First Name(s)', max_length=50)
	last_name = models.CharField('Last Name', max_length=30)
	username = models.CharField('User Name', max_length=30)
	union = models.CharField(blank=True, max_length=30)
	union_no = models.CharField(blank=True, max_length=30)
	age = models.IntegerField(default=0)
	ethnic = models.IntegerField('Ethnic Background', default=0)
	address = models.TextField(blank=True, max_length=320)
	postcode = models.CharField(blank=True, max_length=10)
	phone = models.IntegerField(blank=True, default=0)
	email = models.EmailField(max_length=200)
	photo = models.ImageField(blank=True, max_length=150)
	
	def __str__(self):
		return self.username

class executive (models.Model):
	name = models.CharField(max_length=30)	
	director = models.CharField('Company Director', blank=True, max_length=60)
	contact = models.CharField('Contact Name', blank=True, max_length=60)
	email = models.EmailField(blank=True, max_length=200)
	phone = models.IntegerField(default=0)
	website = models.URLField(max_length=50)
	logo = models.ImageField(blank=True, max_length=150)
	
	def __str__(self):
		return self.name

class location (models.Model):
	name = models.CharField(max_length=30)
	executive = models.ForeignKey(executive)
	add1 = models.CharField('Address Line 1', max_length=80)
	add2 = models.CharField('Address Line 2', blank=True, max_length=80)
	add3 = models.CharField('Address Line 3', blank=True, max_length=80)
	add4 = models.CharField('Address Line 4', blank=True, max_length=80)
	add5 = models.CharField('Address Line 5', blank=True, max_length=80)
	postcode = models.CharField(max_length=10)
	contact = models.CharField(blank=True, max_length=60)
	email = models.EmailField(blank=True, max_length=200)
	phone = models.IntegerField(blank=True, default=0)
	steward1 = models.CharField(blank=True, max_length=60)
	steward2 = models.CharField(blank=True, max_length=60)
	steward3 = models.CharField(blank=True, max_length=60)
	steward4 = models.CharField(blank=True, max_length=60)
	manager = models.CharField('General Manager', blank=True, max_length=60)
	wifi = models.CharField(blank=True, max_length=40)
	logo = models.ImageField(blank=True, max_length=150)
	photo = models.ImageField(blank=True, max_length=150)

	def __str__(self):
		return self.name

class test(models.Model): 
	testno = models.UUIDField('Test No', primary_key=True, default=uuid.uuid4, editable=False)	
	pik = models.CharField('Personal ID Key', max_length=10)
	user = models.ForeignKey(user)
	location = models.ForeignKey(location) #test site is location
	role = models.IntegerField(default=0)
	type = models.IntegerField(default=0)
	start = models.DateTimeField('Start of Service')
	avg_hours = models.DurationField('Average Weekly Hours')
	received = models.DateTimeField('Time/Date Stamp')
	t1 = models.IntegerField(default=0)
	t2 = models.IntegerField(default=0)
	t3 = models.IntegerField(default=0)
	t4 = models.IntegerField(default=0)
	t5 = models.IntegerField(default=0)
	t6 = models.IntegerField(default=0)
	t7 = models.IntegerField(default=0)
	t8 = models.IntegerField(default=0)
	t9 = models.IntegerField(default=0)
	t10 = models.IntegerField(default=0)
	t11 = models.IntegerField(default=0)
	t12 = models.IntegerField(default=0)

	def __str__(self):
		self.testno

class event(models.Model):
	name = models.CharField(max_length=80)
	executive = models.ForeignKey(executive)
	description = models.TextField(blank=True, max_length=600)
	add1 = models.CharField('Address Line 1', max_length=80)
	add2 = models.CharField('Address Line 2', blank=True, max_length=80)
	add3 = models.CharField('Address Line 3', blank=True, max_length=80)
	add4 = models.CharField('Address Line 4', blank=True, max_length=80)
	add5 = models.CharField('Address Line 5', blank=True, max_length=80)
	postcode = models.CharField(max_length=10)
	start = models.DateTimeField('Beginning')
	end = models.DateTimeField('End', blank=True)
	logo = models.ImageField(blank=True, max_length=150)
	photo = models.ImageField(blank=True, max_length=100)
	contact = models.CharField('Contact Name', blank=True, max_length=60)
	email = models.EmailField(max_length=200)
	phone = models.IntegerField()
	website = models.URLField(blank=True, max_length=50)

	def __str__(self):
		return self.name