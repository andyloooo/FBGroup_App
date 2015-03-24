print "How old are you?",
age = raw_input() # use raw_input() instead of input()
print "How tall are you?",
height = raw_input() #takes in input
print "How much do you weigh?",
weight = raw_input()

print "so, you're %r old, %r tall and %r heavy." % (age, height, weight)
# single quote needs to be escaped otherwise it would end the string