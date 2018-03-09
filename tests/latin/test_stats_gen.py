import unittest

from latin.stats_gen import word_to_stats
from latin.sentencer import decline_noun
from latin.declensions import decline
from latin.conjugations import conjugate

# from latin.conjugations import conjugate
from latin.lexicon import nominals, adjectives, verbs

def find_by_lex(words, lex):
    for item in words:
        if item['lex'] == lex:
            return item

class StatsGenTests(unittest.TestCase):

    def test_word_to_stats_noun_acc_sg(self):
        noun = find_by_lex(nominals(), 'agricola')
        noun = decline_noun(noun, False, 'A')
        self.assertEqual('agricola-N-AMS', word_to_stats(noun))
        pass

    def test_word_to_stats_noun_gen_sg(self):
        noun = find_by_lex(nominals(), 'poēta')
        noun = decline_noun(noun, False, 'G')
        self.assertEqual('poēta-N-GMS', word_to_stats(noun))
        pass

    def test_word_to_stats_adj_acc_pl(self):
        adj = find_by_lex(adjectives(), 'antīquus')
        adj = decline(adj, 'A', True, 'M')
        self.assertEqual('antīquus-A-AMP', word_to_stats(adj))
        pass

    def test_word_to_stats_vb_p2s(self):
        verb = find_by_lex(verbs(), 'laudō')
        verb = conjugate(verb, 'P', '2', False)
        self.assertEqual('laudō-P2S', word_to_stats(verb))
