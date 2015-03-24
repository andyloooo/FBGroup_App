## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
## Dog is-a Animal
class Dog(Animal):
	
	def __init__(self, name):
		## Dog has-a name
		self.name = name

## Cat is-a Animal
class Person(object)):
	
	def :
		## Person has-a name
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None

## Employee is a Person
class Employee(Person):

	def __init__(self, name, salary):
		## Employee has a name from _init_ parameter
		super(Employee, self).__init__(name) # looks for method relative to first method
		## Employee has-a salary
		self.salary = salary
		
## Fish is-a object
class Fish(object):
	pass
	
## Salmon is-a Fish
class Salmon(Fish):
	pass
	
## Halibut is-a Fish 
class Halibut(Fish):
	pass
	
## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary's attribute pet is-a satan 
mary.pet = satan

## frank is-a Employee with parameter "Frank" and salary of 120000
frank = Employee("Frank", 120000)

## frank's attribute pet is rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## Harry is-a Halibut
Harry = Halibut()