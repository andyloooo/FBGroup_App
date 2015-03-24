from django.shortcuts import render, HttpResponseRedirect, Http404, render_to_response, redirect
from .forms import EmailForm, JoinForm
from .models import Join
from django.conf import settings

from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def get_ip(request):
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forward:
			ip = x_forward.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = ""
	return ip
	
# str(user_id)[:11].replace('-', '').lower()
import uuid

def get_ref_id(): # loops until finds ref_id that doesn't exist
	ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
	try:
		id_exists =  Join.objects.get(ref_id = ref_id) # checks if ref_id already exists
		get_ref_id()
		# have to do something
	except:
		return ref_id

def home(request): # handles home page
	try:
		join_id = request.session['join_id_ref']
		obj =  Join.objects.get(id=join_id)
		# print "The id is " + str(refer_id) # Join ID
		#print  "The obj is %s" % (obj.email)
	except:
		obj = None
	
	
	# print request.META.get("REMOTE_ADDR")
	# print request.META.get("HTTP_X_FORWARDED_FOR")
	# print request.POST["email"], request.POST["email_2"]
	"""
	# this is using regular Django forms
	form = EmailForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data['email']
		new_join, created = Join.objects.get_or_create(email=email)
		print new_join, created
		print new_join.timestamp
		if created:
			print "This obj was created"
	"""
	# this is using model forms
	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit=False)
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_create(email=email)
		if created:
			new_join_old.ref_id = get_ref_id()
			#add our friend who referred us to our Join Model
			if not obj == None:
				new_join_old.friend = obj
			new_join_old.ip_address = get_ip(request)
			new_join_old.save()
		
		# print all "friends" that joined as a result of main sharer email
		#print Join.objects.filter(friend = obj).count() # not one to one so use filter not get, same as.all().filter()
		#print obj.referral.all().count()
		
			
		# redirect here
		return HttpResponseRedirect("/%s" % (new_join_old.ref_id))
		#new_join.ip_address = get_ip(request)
		#new_join.save()
	
	context = {"form": form}  # context will equal python dictionary, this tells you to connect with html
	template = "home.html"
	return render(request, template, context)

def share(request, ref_id): # handles home page
	#print ref_id
	try:
		join_obj = Join.objects.get(ref_id = ref_id)
		friends_referred = Join.objects.filter(friend = join_obj)
		count = join_obj.referral.all().count()
		ref_url = settings.SHARE_URL + str(join_obj.ref_id)
		context = {"ref_id": join_obj.ref_id, "count": count, "ref_url": ref_url}  # context will equal python dictionary, this tells you to connect with html
		template = "share.html"
		return render(request, template, context)	
	except:
		raise Http404
	
def fb(request): # handles home page
	template = "fb.html"
	return render(request, template)

def members(request):
    context = {}
    template = 'members.html'
    return render(request, template, context)

def logout(request):
    auth_logout(request)
    return redirect('/')
	
	
"""
def home2(request): # handles home page
	form = EmailForm
	context = {"form": form}  # context will equal python dictionary
	template = "home2.html"
	return render(request, template, context)
"""