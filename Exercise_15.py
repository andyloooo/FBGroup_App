#from sys import argv

#script, filename = argv

#txt = open(filename)

#print "Here's you file %r:" % filename
#print txt.read()

print "type the filename again:" # reprints
file_again = raw_input("> ")  # places a dash and asks for input

txt_again = open(file_again) # opens file into txt_again variable

print txt_again.read() # reads txt_again variable and prints it out