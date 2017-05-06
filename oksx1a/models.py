import uuid
from django.db import models
from datetime import datetime


# Create your models here.

class assessment(models.Model):
    # raw assessment data field
    timestamp = models.DateTimeField(null=True, auto_now_add=True)
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

    def total(self):
        t = self.t1 + self.t2 + self.t3 + self.t4 + self.t5 + self.t6 + self.t7 + self.t8 + self.t9 + self.t10 + self.t11 + self.t12
        return t

    def average(self):
        a = self.total()
        b = a / 12
        return b
    
    def __str__(self):
        m = str(self.assessment_no)
        return m

class venue(models.Model):
    # venue type categories
    boat = 'VB'
    construct = 'VC'
    flat = 'VF'
    house = 'VH'
    office = 'VO'
    shop = 'VS'
    unit = 'VU'
    default = 'XD'

    choVenue = (
        (boat, 'Boat'),
        (construct, 'Construction Site'),
        (flat, 'Flat or Apartment'),
        (house, 'House'),
        (office, 'Office'),
        (shop, 'Commercial'),
        (unit, 'Industrial'),
        (default, 'Default'),
    )
    
    
    # raw venue data field
    timestamp = models.DateTimeField(null=True, auto_now_add=True)
    venue_no = models.UUIDField('Venue Ref:', primary_key=True, default=uuid.uuid4, editable=False)
    building = models.CharField('Building Type', max_length=2, choices=choVenue, default=default)
    premises = models.CharField('Premises', blank=True, max_length=30)
    add1 = models.CharField('Address Line 1', blank=True, max_length=80)
    add2 = models.CharField('Address Line 2', blank=True, max_length=80)
    add3 = models.CharField('Address Line 3', blank=True, max_length=80)
    add4 = models.CharField('Address Line 4', blank=True, max_length=80)
    add5 = models.CharField('Address Line 5', blank=True, max_length=80)
    country = models.CharField('Country', blank=True, max_length=30)
    postcode = models.CharField(max_length=10)

    def __str__(self):
        l = str(self.venue_no)
        return self.add1 + " " + self.add2 + "," + self.add3 + "," + self.add4 + "," + self.add5 + "." + self.postcode

class role(models.Model):
    # raw type data field

    # race type categories
    arab = 'RR'
    asian = 'RS'
    black = 'RB'
    latin = 'RL'
    mixed = 'RM'
    white = 'RW'

    #gender type categories
    male = 'GM'
    female = 'GF'
    trans = 'GT'

    #authority type categories
    area = 'AA'
    local = 'AL'
    supervisor = 'AS'
    worker = 'AW'

    # employment security status type categories
    contract = 'EO'
    casual = 'EA'
    employed = 'EE'
    training = 'ET'

    # additional type admin categories
    other = 'XO'
    default = 'XD'

    choRace = (
        (arab, 'Arab'),
        (asian, 'Asian'),
        (black, 'Black'),
        (latin, 'Latin'),
        (mixed, 'Mixed'),
        (white, 'White'),
        (other, 'Other'),
        (default, 'Default'),
    )

    choGender = (
        (male, 'Male'),
        (female, 'Female'),
        (trans, 'Trans'),
        (other, 'Other'),
        (default, 'Default'),
    )

    choStatus = (
        (contract, 'Contracted'),
        (casual, 'Casual'),
        (employed, 'Employed'),
        (training, 'In Training'),
        (default, 'Default'),
    )

    choAuthority = (
        (area, 'Area'),
        (local, 'Local'),
        (supervisor, 'Supervisor'),
        (worker, 'Worker'),
        (default, 'Default'),
    )

    timestamp = models.DateTimeField(null=True, auto_now_add=True)
    role_no = models.UUIDField('Type Ref:', primary_key=True, default=uuid.uuid4, editable=False)
    dob = models.DateField('Date of Birth', blank=True, null=True)
    race = models.CharField('Race', max_length=2, choices=choRace, default=default)
    gender = models.CharField('Gender', max_length=2, choices=choGender, default=default)
    status = models.CharField('Employment Status', max_length=2, choices=choStatus, default=default)
    authority = models.CharField('Authority', max_length=2, choices=choAuthority, default=default)
    start = models.DateField('Start of Service', null=True)
    avg_hours = models.DurationField('Average Weekly Hours', null=True)

    # add age method to calculate age from dob field

    def __str__(self):
        l = str(self.type_no)
        return l

class network(models.Model):
    timestamp = models.DateTimeField(null=True, auto_now_add=True)
    network_no = models.UUIDField('Network Ref:', primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(blank=True, max_length=20)
    email = models.EmailField(max_length=200)
    website = models.URLField(blank=True, max_length=75)
    wifi = models.CharField(blank=True, max_length=225)

    def __str__(self):
        l = str(self.network_no)
        return l

class photo(models.Model):
    timestamp=models.DateTimeField(null=True, auto_now_add=True)
    photo_no = models.UUIDField('Photo Ref:', primary_key=True, default=uuid.uuid4, editable=False)
    photo = models.ImageField(blank=True, max_length=150)

    def __str__(self):
        l = str(self.photo_no)
        return l

class user(models.Model):
    timestamp = models.DateTimeField(null=True, auto_now_add=True)
    first_name = models.CharField('First Name(s)', max_length=50)
    last_name = models.CharField('Last Name', max_length=30)
    username = models.CharField('User Name', max_length=30)
    union = models.CharField(blank=True, max_length=30)
    union_no = models.CharField(blank=True, max_length=30)
    logo = models.ForeignKey(photo, blank=True, null=True, related_name='useLogo')
    photos = models.ManyToManyField(photo, blank=True, related_name='usePhotos')
    address = models.ManyToManyField(venue, blank=True, related_name='useAddress')

    def __str__(self):
        return self.username

class executive (models.Model):
    name = models.CharField(max_length=30)
    sector = models.CharField(blank=True, max_length=100)
    director = models.ForeignKey(user, null=True, blank=True, verbose_name='Director')
    logo = models.ForeignKey(photo, blank=True, null=True, related_name='exeLogo')
    photos = models.ManyToManyField(photo, blank=True, related_name='exePhotos')
    address = models.ForeignKey(venue, blank=True, null=True, related_name='exeAddress')
    contacts = models.ManyToManyField(user, blank=True, related_name='exeContacts')
    stewards = models.ManyToManyField(user, blank=True, related_name='exeStewards')
    comms = models.ForeignKey(network, null=True, blank=True, related_name='exeComms', verbose_name='Network')

    def __str__(self):
        return self.name

class location (models.Model):
    name = models.CharField(max_length=30)
    brand = models.ForeignKey(executive, blank=True, null=True, related_name='locExec')
    manager = models.ForeignKey(user, null=True, blank=True, verbose_name='General Manager')
    logo = models.ForeignKey(photo, blank=True, null=True, related_name='locLogo')
    photos = models.ManyToManyField(photo, blank=True, related_name='locPhotos')
    address = models.ForeignKey(venue, blank=True, null=True, related_name='locAddress')
    contacts = models.ManyToManyField(user, blank=True, related_name='locContacts')
    stewards = models.ManyToManyField(user, blank=True, related_name='locStewards')
    comms = models.ForeignKey(network, null=True, blank=True, related_name='locComms', verbose_name='Network')

    # add total method to calculate total in assessments

    def __str__(self):
        l = str(self.brand)
        return self.name + "(" + l + ")"

class test(models.Model):
    test_no = models.UUIDField('Test Ref:', primary_key=True, default=uuid.uuid4, editable=False)
    pik = models.CharField('Personal ID Key', max_length=10)
    user = models.ForeignKey(user, null=True, blank=True, related_name='tesUser')
    location = models.ForeignKey(location) #test site is location
    roles = models.ForeignKey(role, related_name='tesRoles', null=True, blank=True)
    result = models.ForeignKey(assessment, related_name='tesResult', null=True, blank=True)

    def __str__(self):
        l = str(self.test_no)
        return l

class event(models.Model):
    timestamp = models.DateTimeField(null=True, auto_now_add=True)
    name = models.CharField(max_length=80)
    brand = models.ForeignKey(executive, blank=True, null=True, related_name='eveExec')
    description = models.TextField(blank=True, max_length=600)
    start = models.DateTimeField('Beginning')
    end = models.DateTimeField('End', null=True, blank=True)
    logo = models.ForeignKey(photo, blank=True, null=True, related_name='eveLogo')
    photos = models.ManyToManyField(photo, blank=True, related_name='evePhotos')
    address = models.ForeignKey(venue, blank=True, null=True, related_name='eveAddress')
    contacts = models.ManyToManyField(user, blank=True, related_name='eveContacts')
    comms = models.ForeignKey(network, null=True, blank=True, related_name='eveComms', verbose_name='Network')

    def __str__(self):
        return self.name
