from django.contrib import admin

# Register your models here.


from .models import user, executive, location, test, event, venue, assessment

class userAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 			{'fields': ['username', 'first_name', 'last_name', 'union', 'union_no', 'photo']}),
		('Specifications', 	{'fields': ['age', 'gender', 'ethnic'], 'classes': ['collapse']}),
		('Communications', 	{'fields': ['address', 'email', 'phone'], 'classes': ['collapse']}),
		('Evaluations',		{'fields': ['results'], 'classes': ['collapse']}),
	]

class executiveAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,			{'fields': ['name', 'director', 'sector', 'logo']}),
		('Communications',	{'fields': ['contact1', 'contact2', 'website', 'email', 'phone'], 'classes': ['collapse']}),
	]

class locationAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,			{'fields': ['name', 'company', 'manager', 'logo', 'photo']}),
		('Agents',		{'fields': ['steward1', 'steward2', 'steward3', 'steward4'], 'classes': ['collapse']}),
		('Communications',	{'fields': ['contact1', 'contact2', 'website', 'email', 'phone', 'wifi'], 'classes': ['collapse']}),
	]

class testAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 			{'fields': ['pik', 'user', 'location']}),
		('Details',		{'fields': ['role', 'type', 'start', 'avg_hours', 'received'], 'classes': ['collapse']}),
	]

class eventAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,			{'fields': ['name', 'executive', 'description', 'logo', 'photo']}),
		('Communications',	{'fields': ['contact1', 'contact2', 'website', 'email', 'phone'], 'classes': ['collapse']}),		
	]

admin.site.register(assessment)
admin.site.register(venue)
admin.site.register(user, userAdmin)
admin.site.register(executive, executiveAdmin)
admin.site.register(location, locationAdmin)
admin.site.register(test, testAdmin)
admin.site.register(event, eventAdmin)