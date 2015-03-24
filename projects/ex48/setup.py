try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'decription': 'My Project',
	'author': 'Andrew Liu',
	'url': 'andrewmliu.com',
	'download_url': 'andrewmliu.com',
	'author_email': 'liuandrew878@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME']
	'scripts': []
	'name': 'projectname'
}