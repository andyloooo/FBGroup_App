class Parent(object):
	
	def override(self):
		print "PARENT override()"
		
	def implicit(self):
		print "PARENT implicit()"
	
	def altered(self):
		print "PARENT altered()"

class Child(Parent):
	
	def override(self):
		print "CHILD override()"
		
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered() # calls Parent class with Child class and self as arguments
		print "CHILD, AFTER PARENT altered()"
		
dad = Parent() #dad is a object of class Parent 
son = Child()

dad.implicit() # calll function
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()