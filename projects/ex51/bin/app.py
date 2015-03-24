import web # imports web library

urls = (
	'/hello', 'Index'
)

app = web.application(urls, globals()) # stores urls and class variabless

render = web.template.render('templates/', base="layout") # renders html in templates folder and uses the layout.html to fill in contents of other html code
"""
class Index(object):
	def GET(self):
		form = web.input(name= None, greet=None) # greet set to false value
		
		if form.name and form.greet: #if both have a value
			greeting = "%s, %s" % (form.greet, form.name)
			return render.index(greeting = greeting)
		elif form.name == None and form.greet: # error checking
			return "ERROR: name is required"
		elif form.name and form.greet == None:
			return "ERROR: greet is required"
		else:
			return "ERROR: name and greet is required"
"""

class Index(object):
	def GET(self):
		return render.hello_form() # webpage will call hello_form html
		
	def POST(self):
		form = web.input(name="Nobody", greet="Hello")
		greeting = "%s, %s" % (form.greet, form.name)
		
		if form.name and form.greet: #if both have a value
			greeting = "%s, %s" % (form.greet, form.name)
			return render.index(greeting = greeting) # sends to index html with greeting variable
		elif form.name == None and form.greet: # error checking
			return "ERROR: name is required"
		elif form.name and form.greet == None:
			return "ERROR: greet is required"
		else:
			return "ERROR: name and greet is required"
		
if __name__ == "__main__": # runs app
	app.run()