def add(a, b): # new function declared
	print "ADDING %d + %d" % (a, b)
	return a + b # returns specific value in function
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
print "Let's do some math with just functions!"

age = add(30, 5) # calls functions then sets to variable
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) # divides then multiplies then subtracts then adds
what1 = age + height - divide(iq, 2) * weight # alternative formula for above

print "That becomes: ", what, "Can you do it by hand?"
print what1