from django.contrib import admin
from polls.models import Choice, Question

# Register your models here.

#admin.site.register(Question) #register Question model of polls app

#class ChoiceInLine(admin.StackedInline): #create  stacked  fields
class ChoiceInLine(admin.TabularInline):  # create tabular way of displaying inline objects in a more compact style
	model = Choice
	extra = 3 # extra choics for choice text

class QuestionAdmin(admin.ModelAdmin): # create an object that is an admin.ModelAdmin
	#fields = ['pub_date', 'question_text'] # reorders fields
	fieldsets = [ #split the form into fieldsets
		(None, {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
		]
	inlines = [ChoiceInLine] # addes choices below fields
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date'] #adds filter to sidebar that filters by publishing date Django will automatically provide filter options
	search_fields = ['question_text'] #adds a search box  to teh top of the change list

admin.site.register(Question, QuestionAdmin) # create a model admin object then pass it as the second argument to admin.site.register( ) any time you need to change the admin options for an object
#admin.site.register(Choice) # register Choice with the admin