from django.db import models

# Create your models here.

class Join(models.Model): # everytime change models, migrate database
	email = models.EmailField() # requires unique emails
	friend = models.ForeignKey("self", related_name='referral', null = True, blank = True) #use instead of manytomany, how to relate data to other sets of data
	ref_id = models.CharField(max_length=120, default='ABC', unique = True)
	ip_address = models.CharField(max_length=120, default='ABC')
	timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
	updated = models.DateTimeField(auto_now_add = False, auto_now=True)
	# autonowadd is time when created and auto now is time when updated
	
	def __unicode__(self):
		return "%s" % (self.email) # naming individual instance some name
		
	class Meta:
		unique_together = ("email", "ref_id",) # unique constraint
		

"""		# slower way of adding friends
class JoinFriends(models.Model):
	email = models.OneToOneField(Join, related_name = "Sharer") # can only have one
	friends = models.ManyToManyField(Join, related_name= "Friend", null = True, blank = True) # can have many
	
	emailall = models.ForeignKey(Join, related_name='emailall')
	
	def __unicode__(self):
		print "friends are ", self.friends.all()
		print self.emailall
		print self.email
		return self.email.email
"""