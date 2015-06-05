from nose.tools import *
from ex48 import parser

def test_peek():
	word_list = [('verb', 'go'), ('direction', 'north'), ('stop', 'at'), ('noun', 'door')]
	assert_equal(parser.peek(word_list), 'verb')
	empty_word_list = []
	assert_equal(parser.peek(empty_word_list), None)

