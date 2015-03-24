from sys import argv

script, input_file = argv #get text file name from command line

def print_all(f):
	print f.read() # reads the contents of the file
	
def rewind(f):
	f.seek(0) # sets back to the start of the file

def print_a_line(line_count, f):
	print line_count, f.readline() #reads line count then one line
	
current_file = open(input_file) # open input_file into current_file

print "First let's print the whole file:\n"

print_all(current_file) # print contents of current_file using print_all function

print "Now let's rewind, kind of like a tape."

rewind(current_file) # calls rewind function

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file) # calls print_a_line function

current_line += 1 # current_line = current_line + 1
print_a_line(current_line, current_file)

current_line += 1 # current_line = 3
print_a_line(current_line, current_file)