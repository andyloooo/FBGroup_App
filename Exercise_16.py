from sys import argv

script, filename = argv # takes script name and txt name you want

print "We're going to erase %r." % filename # prints questions
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?") # user prompt

print "Opening the file..."
target = open(filename, 'w') # open txt file into target variable in write mode

print "Truncating the file. Goodbye!"
# target.truncate() # empties file but open with 'w' already truncates file

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ") # user prompts after printing line number
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%s\n%s\n%s\n" % (line1, line2, line3)) # incorporates next 6 lines here
# place string and variable substitution inside write(...)
#target.write(line1) # write line1
#target.write("\n") # write new line
#target.write(line2) # write line 2
#target.write("\n") # write new line
#target.write(line3)
#target.write("\n")

target = open(filename, 'r') # have to open file in read mode because before it was in write mode
print target.read()

print "And finally, we close it."
target.close() # close txt file
