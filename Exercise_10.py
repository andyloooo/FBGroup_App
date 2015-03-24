tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
# tab
fat_cat = """ 
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
""" # escape tab sequence
# single quote is the same as double quote
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# below code is an infinite loop the just prints the array
# while True: 
#	for i in ["/","-","|","\\","|"]:
#		print "%s\r" % i,