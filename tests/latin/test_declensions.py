import unittest

from latin.declensions import decline
from latin.lexicon import nominals
from latin.utils import find_by_lex

class DeclensionsTests(unittest.TestCase):

    def test_decline_2nd_decl_vir(self):
        noun = find_by_lex(nominals(), 'vir')
        noun = decline(noun, 'A', False, 'M')
        self.assertEqual(noun['inflected'], 'virum')
        self.assertEqual(noun['parsing'], 'AMS')

    def test_decline_2nd_decl_vir_nom_sg(self):
        noun = find_by_lex(nominals(), 'vir')
        noun = decline(noun, 'N', False, 'M')
        self.assertEqual(noun['inflected'], 'vir')
        self.assertEqual(noun['parsing'], 'NMS')
