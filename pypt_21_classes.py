class computer(object):
	def __init__(self, buttons):
		self.buttons = buttons # attribute of object
	print "buttons" # prints when calculator is made

class calculator(computer): # calculator is an object
	
	def __init__(self, x, y):
		self.x = x # intialize x and y values in class
		self.y = y
		print "x = ", x
		print "y = ", y
	
	def addition(self): # takes self parameters
		added = self.x + self.y
		print "add = ", added
	
	def subtraction(self):
		sub = self.x - self.y
		print "subtract = ", sub
	
	def multiplication(self):
		mult = self.x * self.y
		print "multiply = ", mult
	
	def division(self):
		div = self.x / self.y
		print "divide = ", div

x = float(3) # makes sure floating point operations return decimal values
y = float(5)		
calculate = calculator(x,y) # set calculate to an instance of class calculator
calculate.addition() #
calculate.multiplication()
calculate.subtraction()
calculate.division()

calculator.buttons = "lots"
print calculator.buttons