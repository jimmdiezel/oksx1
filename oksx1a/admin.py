from django.contrib import admin

# Register your models here.


from .models import user, executive, location, test, event

admin.site.register(user)
admin.site.register(executive)
admin.site.register(location)
admin.site.register(test)
admin.site.register(event)