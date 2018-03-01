import unittest

from latin.lexicon import nominals, adjectives
from latin.sentencer import decline_noun, append_modifiers_to_noun

def find_by_lex(words, lex):
    for item in words:
        if item['lex'] == lex:
            return item

class SentencerTests(unittest.TestCase):

    def test_decline_noun(self):
        noun = find_by_lex(nominals(), 'agricola')
        declined = decline_noun(noun, True, 'G')

        self.assertEqual(declined['is_plural'], True)
        self.assertEqual(declined['case'], 'G')
        self.assertEqual(declined['number'], 'P')
        self.assertEqual(declined['inflected'], 'agricolārum')
        self.assertEqual(declined['modifiers'], [])

    def test_append_modifiers_to_noun(self):
        noun = find_by_lex(nominals(), 'agricola')
        declined = decline_noun(noun, True, 'G')
        adj = find_by_lex(adjectives(), 'magnus')
        append_modifiers_to_noun(declined, adjectives, adj)

        self.assertEqual(declined['is_plural'], True)
        self.assertEqual(declined['case'], 'G')
        self.assertEqual(declined['number'], 'P')
        self.assertEqual(declined['inflected'], 'agricolārum')
        decl_adj = declined['modifiers'][0]
        self.assertEqual(decl_adj['is_plural'], True)
        self.assertEqual(decl_adj['case'], 'G')
        self.assertEqual(decl_adj['number'], 'P')
        self.assertEqual(decl_adj['inflected'], 'magnōrum')
