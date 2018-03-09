import unittest

from latin.conjugations import conjugate
from latin.lexicon import verbs

def find_by_lex(words, lex):
    for item in words:
        if item['lex'] == lex:
            return item

class ConjugationsTests(unittest.TestCase):

    def helper(self, verb_text, parsing, expected):
        verb = find_by_lex(verbs(), verb_text)
        is_plural = True if parsing[2] == 'P' else False
        verb = conjugate(verb, parsing[0], parsing[1], is_plural)
        self.assertEqual(verb['inflected'], expected)

    def test_conjugate_first_pres_sing(self):
        self.helper('amō', 'P2S', 'amās')

    def test_conjugate_first_pres_plural(self):
        self.helper('laudō', 'P3P', 'laudant')

    def test_conjugate_first_future(self):
        self.helper('laudō', 'F2S', 'laudābis')

    def test_conjugate_first_imperfect(self):
        self.helper('laudō', 'I2P', 'laudābātis')

    def test_conjugate_second_present(self):
        self.helper('moneō', 'P2S', 'monēs')

    def test_conjugate_second_future(self):
        self.helper('moneō', 'F2S', 'monēbis')

    def test_conjugate_second_imperfect(self):
        self.helper('moneō', 'I3S', 'monēbat')
