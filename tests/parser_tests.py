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

def test_skip():
	word_list = [('verb', 'go'), ('direction', 'north'), ('stop', 'at'), ('noun', 'door')]
	parser.skip(word_list, 'verb')
	assert_equal(word_list, [('direction', 'north'), ('stop', 'at'), ('noun', 'door')])

def test_parse_verb():
	word_list = [('verb', 'go'), ('direction', 'north'), ('stop', 'at'), ('noun', 'door')]
	assert_equal(parser.parse_verb(word_list), ('verb', 'go'))
	word_list = [('direction', 'north'), ('stop', 'at'), ('noun', 'door')]
	assert_raises(parser.ParserError, parser.parse_verb, word_list)

def test_parse_object(): 
	word_list = [('noun', 'door'), ('verb', 'go'), ('direction', 'north'), ('stop', 'at')]
	assert_equal(parser.parse_object(word_list), ('noun', 'door'))
	word_list = [('direction', 'north'), ('stop', 'at')]
	assert_equal(parser.parse_object(word_list), ('direction', 'north'))
	word_list = [('verb', 'go'), ('direction', 'north'), ('stop', 'at')]
	assert_raises(parser.ParserError, parser.parse_object, word_list)

def test_parse_subject():
	word_list = [('noun', 'door'), ('verb', 'go'), ('direction', 'north'), ('stop', 'at')]
	assert_equal(parser.parse_subject(word_list), ('noun', 'door'))
	word_list = [('verb', 'go'), ('direction', 'north'), ('stop', 'at')]
	assert_equal(parser.parse_subject(word_list), ('noun', 'player'))
	word_list = [('direction', 'north'), ('stop', 'at')]
	assert_raises(parser.ParserError, parser.parse_subject, word_list)
	word_list = [('stop', 'at'), ('direction', 'north')]
	assert_raises(parser.ParserError, parser.parse_subject, word_list)

def test_parse_sentence():
	word_list = [('noun', 'man'), ('verb', 'go'), ('direction', 'north'), ('stop', 'at'), ('noun', 'door')]
	s = parser.parse_sentence(word_list)
	assert_equal(s.to_tuple(), ('man', 'go', 1, 'north'))
	word_list = [('noun', 'man'), ('verb', 'go'), ('number', 5), ('stop', 'at'), ('noun', 'door')]
	s = parser.parse_sentence(word_list)
	assert_equal(s.to_tuple(), ('man', 'go', 5, 'door'))
	word_list = [('stop', 'in'), ('verb', 'eat'), ('noun', 'door')]
	s = parser.parse_sentence(word_list)
	assert_equal(s.to_tuple(), ('player', 'eat', 1, 'door'))
	word_list = [('direction', 'north'), ('verb', 'eat'), ('noun', 'door')]
	assert_raises(parser.ParserError, parser.parse_sentence, word_list)

def test_unknown_words():
	word_list = [('noun', 'man'), ('verb', 'go'), ('direction', 'north'), ('stop', 'at'), ('xxx', 'xxx'), ('noun', 'door')]
	s = parser.parse_sentence(word_list)
	assert_raises(parser.ParserError, parser.parse_sentence, word_list)
	word_list = [('stop', 'the'), ('verb', 'go'), ('direction', 'north')]
	s = parser.parse_sentence(word_list)
	assert_raises(parser.ParserError, parser.parse_sentence, word_list)