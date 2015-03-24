age = raw_input("How old are you? ") # Prints question and inputs into variable
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight) # will output in numbers with single quotes around them
# single quote for foot inside single quotes will have escape sequence because of %r
# change %r to %s for output without escape sequences and single quotes