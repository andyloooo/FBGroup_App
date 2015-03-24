def scan(input):
	scan_check = [] # makes array to put tuples in
	input_split = input.split() # makes array with words of input
	
	directions = ['north', 'south', 'east', 'west', 'down', 'left', 'right', 'back']
	verbs = ['go', 'stop', 'kill', 'eat'] # sets lists of verbs
	stop_words = ['the', 'in', 'of', 'from', 'at', 'it'] # sets lists of stop_words
	nouns = ['door', 'bear', 'princess', 'cabinet']
	
	for word in input_split:	
		if word.isdigit(): # checks if word is a number
			int_convert = int(word) # converts string to number
			scan_check.append(('number',int_convert)) # makes number tuple
		else:
			word_raw = word #retains capitalization
			word = word.lower() #makes lowercase to check in lists
			if word in directions: # checks if item is in directions list
				scan_check.append(('direction', word_raw)) # makes direction tuple
			elif word in verbs: # checks if item is in verbs list
				scan_check.append(('verb', word_raw)) # makes verb tuple
			elif word in stop_words: # checks if item is in stop_words list
				scan_check.append(('stop', word_raw)) # makes stop tuple
			elif word in nouns: # checks if word is in nouns list
				scan_check.append(('noun', word_raw)) # makes noun tuple
			else:
				scan_check.append(('error', word_raw)) # makes error tuple
	
	return scan_check # returns tuple to check against tuple in lexicon_test.py
	
input = raw_input("Enter string> ")
print scan(input)