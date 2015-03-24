from django.contrib import admin

# Register your models here.
from .models import Join # looks in same folder for models.py

class JoinAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'friend', 'timestamp', 'updated']
	
	class Meta:
		model = Join

admin.site.register(Join, JoinAdmin)