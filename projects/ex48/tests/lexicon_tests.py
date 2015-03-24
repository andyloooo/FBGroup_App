from nose.tools import *
from ex48 import lexicon

def test_directions():
	assert_equal(lexicon.scan('north'), [('direction', 'north')]) # tests the tuple when 'north' is entered
	result = lexicon.scan("north south east") # tests tuple when string is entered
	assert_equal(result, [('direction', 'north'),
							('direction', 'south'),
							('direction', 'east')])

def test_verbs():
	assert_equal(lexicon.scan("go"), [('verb', 'go')]) # tests the tuple 
	result = lexicon.scan("go kill eat") # tests tuple when string is entered
	assert_equal(result, [('verb', 'go'),
							('verb', 'kill'),
							('verb', 'eat')])
							
def test_stops():
	assert_equal(lexicon.scan("the"), [('stop', 'the')]) # tests the tuple 
	result = lexicon.scan("the in of") # tests tuple when string is entered
	assert_equal(result, [('stop', 'the'),
							('stop', 'in'),
							('stop', 'of')])

def test_nouns():
	assert_equal(lexicon.scan("bear"), [('noun', 'bear')]) # tests the tuple 
	result = lexicon.scan("bear princess") # tests tuple when string is entered
	assert_equal(result, [('noun', 'bear'),
							('noun', 'princess')])
							
def test_numbers():
	assert_equal(lexicon.scan("1234"), [('number', 1234)]) # tests the tuple 
	result = lexicon.scan("3 91234") # tests tuple when string is entered
	assert_equal(result, [('number', 3),
							('number', 91234)])
							
def test_errors():
	assert_equal(lexicon.scan("ASDFADFASDG"),[('error','ASDFADFASDG')]) # tests the tuple 
	result = lexicon.scan("bear IAS princess") # tests tuple when string is entered
	assert_equal(result, [('noun', 'bear'), 
						('error', 'IAS'), 
						('noun', 'princess')])