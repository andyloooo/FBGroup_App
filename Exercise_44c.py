class Parent(object):
	
	def altered(self):
		print "PARENT altered()"

class Child(Parent):
	
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered() # takes current class then self as arguments to find position in Method Resolution Order and prints Parent.altered()
		print "CHILD, AFTER PARENT altered()" 
		
dad = Parent() # create object that is a Parent
son = Child()

dad.altered() # call function
son.altered()