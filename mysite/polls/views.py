#from django.template import RequestContext, loader # not needed with new shortcut
from django.http import HttpResponse, Http404
from django.shortcuts import  get_object_or_404, render
from polls.models import Question

# Create your views here.

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
	"""
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'polls/detail.html', {'question': question})
	"""
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question}) # quicker way of  writing the above
	
def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s" % question_id)
	
def index(request): # shortcut for loading a template,. filling a context and returning an HttpResponse object
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('polls/index.html') # loads the template called polls/index.html and passes it a context
	#context = RequestContext(request, {
	#	'latest_question_list': latest_question_list,
	#	})
	
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)
	#return HttpResponse(template.render(context))