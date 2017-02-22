import uuid
from django.db import models

# Create your models here.

class assessment(models.Model):
	assessment_no = models.UUIDField('Assessment Ref:', primary_key=True, default=uuid.uuid4, editable=False)
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
		m = str(self.assessment_no)
		return m

class venue(models.Model):
	venue_no = models.UUIDField('Venue Ref:', primary_key=True, default=uuid.uuid4, editable=False)
	add1 = models.CharField('Address Line 1', blank=True, max_length=80)
	add2 = models.CharField('Address Line 2', blank=True, max_length=80)
	add3 = models.CharField('Address Line 3', blank=True, max_length=80)
	add4 = models.CharField('Address Line 4', blank=True, max_length=80)
	add5 = models.CharField('Address Line 5', blank=True, max_length=80)
	postcode = models.CharField(max_length=10)

	def __str__(self):
		l = str(self.company)
		return self.add1 + " " + self.add2 + "," + self.add3 + "," + self.add4 + "," + self.add5 + "." + "postcode"

class type(models.Model):
	type_no = models.UUIDField('Type Ref:', primary_key=True, default=uuid.uuid4, editable=False)
	age = models.IntegerField(default=0, blank=True)
	gender = models.IntegerField(default=0, blank=True)
	ethnic = models.IntegerField('Ethnic Background', blank=True, default=0)
	
	def __str__(self):
		l = str(self.type_no)
		return l

class network(models.Model):
	network_no = models.UUIDField('Network Ref:', primary_key=True, default=uuid.uuid4, editable=False)	
	phone = models.CharField(blank=True, max_length=20)
	email = models.EmailField(max_length=200)
	website = models.URLField(max_length=75)
	wifi = models.CharField(blank=True, max_length=225)
	address = models.ManyToManyField(venue, blank=True, related_name='useAddress')

	def __str__(self):
		l = str(self.type_no)
		return l

class user(models.Model):
	first_name = models.CharField('First Name(s)', max_length=50)
	last_name = models.CharField('Last Name', max_length=30)
	username = models.CharField('User Name', max_length=30)
	union = models.CharField(blank=True, max_length=30)
	union_no = models.CharField(blank=True, max_length=30)
	photo = models.ImageField(blank=True, max_length=150)
	average = models.ForeignKey(assessment, default=0, blank=True, related_name='useResults')
	

	def __str__(self):
		return self.username

class executive (models.Model):
	name = models.CharField(max_length=30)	
	sector = models.CharField(blank=True, max_length=100)
	director = models.ForeignKey(user, null=True, blank=True, verbose_name='Director')
	contact1 = models.ForeignKey(user, null=True, blank=True, related_name='exeContact1', verbose_name='Contact 1')
	contact2 = models.ForeignKey(user, null=True, blank=True, related_name='exeContact2', verbose_name='Contact 2')
	logo = models.ImageField(blank=True, max_length=150)
	
	
	def __str__(self):
		return self.name

class location (models.Model):
	name = models.CharField(max_length=30)
	company = models.ForeignKey(executive)
	steward1 = models.ForeignKey(user, null=True, blank=True, related_name='locSteward1', verbose_name='Steward 1')
	steward2 = models.ForeignKey(user, null=True, blank=True, related_name='locSteward2', verbose_name='Steward 2')
	steward3 = models.ForeignKey(user, null=True, blank=True, related_name='locSteward3', verbose_name='Steward 3')
	steward4 = models.ForeignKey(user, null=True, blank=True, related_name='locSteward4', verbose_name='Steward 4')
	manager = models.ForeignKey(user, null=True, blank=True, verbose_name='General Manager')
	contact1 = models.ForeignKey(user, null=True, blank=True, related_name='locContact1', verbose_name='Contact 1')
	contact2 = models.ForeignKey(user, null=True, blank=True, related_name='locContact2', verbose_name='Contact 2')
	logo = models.ImageField(blank=True, max_length=150)
	photo = models.ImageField(blank=True, max_length=150)

	def __str__(self):
		l = str(self.company)
		return self.name + "(" + l + ")"

class test(models.Model):
	test_no = models.UUIDField('Test Ref:', primary_key=True, default=uuid.uuid4, editable=False) 
	pik = models.CharField('Personal ID Key', max_length=10)
	user = models.ForeignKey(user, null=True, blank=True)
	location = models.ForeignKey(location) #test site is location
	role = models.IntegerField(null=True, blank=True)
	type = models.IntegerField(null=True, blank=True)
	start = models.DateField('Start of Service')
	avg_hours = models.DurationField('Average Weekly Hours')
	received = models.DateTimeField('Time/Date Stamp')
	result = models.ForeignKey(assessment, related_name='tesResult', null=True, blank=True)

class event(models.Model):
	name = models.CharField(max_length=80)
	executive = models.ForeignKey(executive)
	description = models.TextField(blank=True, max_length=600)
	start = models.DateTimeField('Beginning')
	end = models.DateTimeField('End', blank=True)
	logo = models.ImageField(blank=True, max_length=150)
	photo = models.ImageField(blank=True, max_length=100)
	contact1 = models.ForeignKey(user, null=True, blank=True, related_name='eveContact1', verbose_name='Contact 1')
	contact2 = models.ForeignKey(user, null=True, blank=True, related_name='eveContact2', verbose_name='Contact 2')

	def __str__(self):
		return self.name