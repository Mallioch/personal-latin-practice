
from latin import lexicon
from latin import sentencer
from latin.stats_gen import word_to_stats
from english import englisher
import random
import sys


class colors:
    '''Colors class:
    reset all colors with colors.reset
    two subclasses fg for foreground and bg for background.
    use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.green
    also, the generic bold, disable, underline, reverse, strikethrough,
    and invisible work with the main class
    i.e. colors.bold
    '''
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'


def create_sentence():
    construct = sentencer.create(lexicon.nominals(), lexicon.verbs(), lexicon.personal_pronouns(), lexicon.adverbs(), lexicon.adjectives(), lexicon.specials())


    foreign = []
    stats = []
    english = []

    pronoun = englisher.pronoun(construct)
    if pronoun != '':
        english.append(pronoun)

    for word in construct['sent']:

        # words with modifiers
        word_type = word['word-type']
        if word_type == 'verb' or word_type == 'nominal':

            # put adjectives after nouns
            if word_type == 'nominal':
                if 'inflected' not in word:
                    print('no inflected', word)
                foreign.append(word['inflected'])

            for mod in word['modifiers']:
                english.append(mod['glosses'][random.randint(0, len(mod['glosses']) - 1)])
                stats.append(word_to_stats(mod))
                if 'inflected' in mod:
                    foreign.append(mod['inflected'])
                else:
                    foreign.append(mod['lex'])

            # put adverbs before verbs
            if word_type == 'verb':
                print('word', word)
                foreign.append(word['inflected'])


        else:
            foreign.append(word['lex'])


        word_text = word['glosses'][random.randint(0, len(word['glosses']) - 1)]
        if word_type == 'verb':
            word_text = '[' + word['english_tense'] + ']' + word_text


        english.append(word_text)

        if word_type == 'verb':
            print('person', construct['person'], 'number', construct['number'])
            stats.append(word_type + '-' + word['lex'] + '-' + construct['person'] + '-' + str(construct['number']))
        else:
            stats.append(word_type + '-' + word['lex'])

    print(chr(27) + "[2J")
    print('latin', colors.fg.blue + ' '.join(str(x) for x in foreign) + colors.reset)
    print('stats', '|'.join(str(x) for x in stats))
    print('english', colors.fg.green + ' '.join(str(x) for x in english) + colors.reset)

def random_pos(pos):
    list = lexicon.adjectives()
    if pos == 'nominal':
        list = lexicon.nominals()
    elif pos == 'verb':
        list = lexicon.verbs()
    output = []
    for x in range(0, 7):
        r = random.randint(0, len(list) - 1)
        output.append(list[r])
        del(list[r])

    for item in output:
        print(item['lex'])


if len(sys.argv) < 2:
    print('')
    print('You need to specify a command, like the following:')
    print('\t' + colors.fg.blue + 'python main.py sentence' + colors.fg.darkgrey + ' # returns a generated sentence' + colors.reset)
    print('\t' + colors.fg.blue + 'python main.py rand adj' + colors.fg.darkgrey + ' # returns a list of random adjectives' + colors.reset)
    print('')
else:
    if sys.argv[1] == 'sentence':
        create_sentence()
    elif sys.argv[1] == 'rand':
        random_pos(sys.argv[2])
