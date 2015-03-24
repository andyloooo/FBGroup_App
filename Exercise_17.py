from sys import argv
from os.path import exists

#script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

indata = open(from_file).read() # open contents of from_file and reads it into indata
#indata = in_file.read()

#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exist %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CRTL-C to abort"
#raw_input()

out_file = open(to_file, 'w') # opens file into new variable and truncates file if it already exists
out_file.write(indata) # writes contents of indata into out_file

#print "Alright, all done"

out_file.close() # you have to close file after opening it or writing to it
#in_file.close()