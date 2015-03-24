class Parent(object):
	pass

class Child(Parent):
	
	def __init__(self, stuff):
		self.stuff = stuff
		#super(Child, self).__init__() #initialize in child first, rather than parent
		
child = Child("stuff")

print child.stuff


class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg

class ElectricCar(Car):
    def __init__(self, battery_type, model, color, mpg):
        self.battery_type=battery_type
        super(ElectricCar, self).__init__(model, color, mpg) # sends paramaters up to be initialized through the Car class as ElectricCar class doesn't contain model, color, mg

car = ElectricCar('battery', 'ford', 'golden', 10)
print car.__dict__
