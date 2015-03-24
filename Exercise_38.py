ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ') # separator of 1 space
print stuff
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: # while length of stuff is less than 10
	next_one = more_stuff.pop() # removes and returns the last item in list
	print "Adding: ", next_one
	stuff.append(next_one) # append next_one to end of stuff
	print "there are %d items now." % len(stuff)
	
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop() # removes and returns the last item in list
print ' '.join(stuff) # concatenates stuff in list into string with 1 space in between
print '#'.join(stuff[3:6]) # concatenates from items 3 - 5 with a # in between