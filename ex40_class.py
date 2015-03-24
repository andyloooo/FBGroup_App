class MyStuff(object): # this is a blueprint for building a copy of that type of thing
	
	def __init__(self): # initializes empty object called self
		self.tangerine = "And now a thousand years between"
		# set variables on self object
	def apple(self):
		print "I AM CLASSY APPLES!"

thing = MyStuff()
thing.apple()
print thing.tangerine # takes self object and assign it to thing variable