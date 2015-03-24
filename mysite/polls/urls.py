from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name ='index'),
	#ex. /polls/5
	url(r'^(?P<question_id>\d+)/$', views.detail, name = 'detail'), # formatting URL links to a cetrain style, calling the views.py  methods
	#ex. /polls/5/results
	url(r'^(?P<question_id>\d+)/results/$', views.results, name = 'results'),
	#ex. /polls/5/vote
	url(r'^(?P<question_id>\d+)/vote/$', views.vote, name = 'vote'),
	)

