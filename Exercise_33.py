i = 0
numbers = [] # declare list

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i) # appends to the end of list
	
	i += 1 # adds 1 to i
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

	
print "The numbers: "

for num in numbers: # print out list
	print num
	
i = 0
x = 6 # limiting integer
n = 2 # increment value
numbers1 = []


def function(i, x, n, numbers): # declare function and arguments
	if i < x: 
		print "At the top i is %d" % i
		numbers.append(i)
		
		i += n
		
		print "Numbers2 now: ", numbers
		print "At the bottom i is %d" % i
		function(i, x, n, numbers) # recursive function that calls itself outputs same as while loop

function(i, x, n, numbers1) # call function with arguments

for num in numbers1: # print out list
	print num

numbers2 = []

for i in range(0, x): # for loop with range increments by 1, already initialized at 1
	print "At the top i is %d" % i
	
	numbers2.append(i)
	
	print "Numbers2 now: ", numbers2
	print "At the bottom i is %d" % i
		
for num in numbers2: # print out list
	print num