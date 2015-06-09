from nose.tools import *
from ex48 import parser

def test_peek():
	word_list = [('verb', 'go'), ('direction', 'north'), ('stop', 'at'), ('noun', 'door')]
	assert_equal(parser.peek(word_list), 'verb')
	empty_word_list = []
	assert_equal(parser.peek(empty_word_list), None)

def test_match():
	word_list = [('verb', 'go'), ('direction', 'north'), ('stop', 'at'), ('noun', 'door')]
	assert_equal(parser.match(word_list, 'verb'), ('verb', 'go'))
	assert_equal(parser.match(word_list, 'stop'), None)
	assert_equal(parser.match(None, 'noun'), None)
