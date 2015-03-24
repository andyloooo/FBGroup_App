from sys import argv

script, user_name = argv # modifies input to not only include program name but also user_name
prompt = '> ' # just equals string

print "Hi %s I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt) # enters string before input

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r Computer. Nice.
""" % (likes, lives, computer)