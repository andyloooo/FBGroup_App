sentence = "1 2345 12344"

words = sentence.split()
numbers = []

for word in words:
	number = int(word)
	numbers.append(number)

print numbers