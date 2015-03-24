class Song(object):
	def __init__(self, lyrics): # attribute of self not actual variable instantiate
	# attribute to new object that will be created
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"]) 
	# You instantiate (create) a class by calling the class like it's a function, like this:
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])
						
happy_bday.sing_me_a_song()

print happy_bday.lyrics

bulls_on_parade.sing_me_a_song()