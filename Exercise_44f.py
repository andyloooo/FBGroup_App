# Composition

class Other(object): # create Other class
		
	def override(self):
		print "OTHER override()"
	
	def implicit(self):
		print "OTHER implicit()"
	
	def altered(self):
		print "OTHER altered()"

class Child(object):
	
	def __init__(self):
		self.other = Other() # creates object that is in self.other
	
	def implicit(self):
		self.other.implicit() # prints other.implicit()
	
	def override(self):
		print "CHILD override()" # prints son.override()
	
	def altered(self):
		print "CHILD, BEFORE OTHER altered()"
		self.other.altered() # prints "OTHER altered()"
		print "CHILD, AFTER OTHER altered()"

son = Child() # son is a child

son.implicit()
son.override()
son.altered()
