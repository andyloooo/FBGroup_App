class Parent(object):
	
	def implicit(self):
		print "Parent implicit()"
		
class Child(Parent): # inherit Parent's functions
	pass

dad = Parent()
son = Child()

dad.implicit() # same function
son.implicit()	# calls implied function from Parent object