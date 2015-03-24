import web

urls = (
	'/', 'Index', '/foo', 'Foo' # defines url path and corresponding class
)

app = web.application(urls, globals())

render = web.template.render('templates/') # renders html in this directory

class Index(object): # called at homepage
	def GET(self):
		greeting = "Hello World"
		return render.index(greeting = greeting) # passes through variable to html file

class Foo(object): # called at website/foo
	def GET(self):
		andrew = "andyloooo"
		return render.foo(andrew = andrew) # passes through variable to html file
		
if __name__ == "__main__":
	app.run()