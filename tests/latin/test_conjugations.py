import unittest

from latin.conjugations import conjugate
from latin.lexicon import verbs

def find_by_lex(words, lex):
    for item in words:
        if item['lex'] == lex:
            return item

class ConjugationsTests(unittest.TestCase):

    def test_conjugate_first_a_sing(self):
        verb = find_by_lex(verbs(), 'amō')
        conjugate(verb, 'p', '2', is_plural = False)
        self.assertEqual(verb['inflected'], 'amās')

    def test_conjugate_first_a_plural(self):
        verb = find_by_lex(verbs(), 'laudō')
        conjugate(verb, 'p', '3', is_plural = True)
        self.assertEqual(verb['inflected'], 'laudant')
