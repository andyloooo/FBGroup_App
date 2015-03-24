class Parent(object):
	
	def override(self):
		print "PARENT override()"

class Child(Parent):

	def override(self): # overrides override function in PARENT
		print "CHILD override()"
		
dad = Parent()
son = Child()

dad.override() # calls override function in dad
son.override() # calls override function in son instead of the one in dad