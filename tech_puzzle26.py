def checker(x, digits_array):
	x_string = str(x) # turn x into string
	x_list = list(x_string) # turn x string into list
	count = 0
	for i in range(-4,0):
		if x_list[i] == digits_array[i]:
			count+=1
	
	if count == 4:
		print "Awesome"
		return True
	else:
		return False
		
	
def maker():
	
	for i in range(1000, 50000):
		x = i
		x_squared = x**2
		
		digits_string = str(x_squared)
		
		digits_list = list(digits_string)
		
		checked = checker(x, digits_list) # check digits in each case
		if checked:
			print x, """ 
			
			"""
	

maker()