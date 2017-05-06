from django.contrib import admin

# Register your models here.


from .models import user, executive, location, test, event, venue, assessment, role, network

class assessmentAdmin(admin.ModelAdmin):
    list_display = ('t1','t2','t3','t4','t5','t6','t7','t8','t9','t10','t11','t12','total','average')

class userAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, 			{'fields': ['username', 'first_name', 'last_name', 'union', 'union_no', 'photos']}),
        ('Details',             {'fields': ['address'], 'classes': ['collapse']}),
    ]
    list_display = ('username', 'first_name', 'last_name', 'union', 'union_no')

class executiveAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,			{'fields': ['name', 'director', 'sector', 'logo', 'photos']}),
        ('Details',	        {'fields': ['address', 'comms', 'contacts', 'stewards'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'director', 'sector')

class locationAdmin(admin.ModelAdmin):
    fieldsets = [
	(None,			{'fields': ['name', 'brand', 'manager', 'logo', 'photos']}),
	('Details',	        {'fields': ['address', 'comms', 'contacts', 'stewards'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'brand', 'manager')

class testAdmin(admin.ModelAdmin):
    fieldsets = [
	(None, 			{'fields': ['pik', 'user', 'location']}),
	('Details',		{'fields': ['roles'], 'classes': ['collapse']}),
        ('Assessment',          {'fields': ['result']}),
    ]
    list_display = ('pik', 'user', 'location')

class eventAdmin(admin.ModelAdmin):
    fieldsets = [
	(None,			{'fields': ['name', 'brand', 'description', 'start', 'end', 'logo']}),
	('Communications',	{'fields': ['contacts'], 'classes': ['collapse']}),		
    ]
    list_display = ('name', 'brand', 'start', 'end')

admin.site.register(role)
admin.site.register(network)
admin.site.register(assessment, assessmentAdmin)
admin.site.register(venue)
admin.site.register(user, userAdmin)
admin.site.register(executive, executiveAdmin)
admin.site.register(location, locationAdmin)
admin.site.register(test, testAdmin)
admin.site.register(event, eventAdmin)
