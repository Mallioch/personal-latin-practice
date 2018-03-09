import random
from .declensions import decline
from .conjugations import conjugate

def filter(key, val, arr):
    output = []
    for item in arr:
        if item[key] == val:
            output.append(item)

    return output

def decline_noun(noun, is_plural, case):
    obj = dict(noun)
    #print('modify_noun', noun['lex'])
    obj['modifiers'] = []
    obj['is_plural'] = is_plural
    obj['case'] = case
    obj['number'] = 'P' if is_plural else 'S'
    obj['inflected'] = obj['lex']
    obj = decline(obj, case, is_plural, obj['gender'])
    return obj

def append_modifiers_to_noun(noun, adjectives, adj_to_add = None):
    new_adj = None

    if adj_to_add == None:
        if random.randint(0, 2) == 1:
            new_adj = dict(adjectives[random.randint(0, len(adjectives) - 1)])
    else:
        new_adj = adj_to_add

    if new_adj != None:
        new_adj['inflected'] = new_adj['lex']
        new_adj['is_plural'] = noun['is_plural']
        new_adj['case'] = noun['case']
        new_adj['number'] = noun['number']
        new_adj = decline(new_adj, noun['case'], noun['is_plural'], noun['gender'])
        noun['modifiers'].append(new_adj)


def modify_verb(person, is_plural, verb, adverbs, specials):
    verb['modifiers'] = []

    # print('teh person', person)
    tense = 'P'
    verb['english_tense'] = 'present'
    tense_rand = random.randint(1, 3)
    if tense_rand == 1:
        tense = 'F'
        verb['english_tense'] = 'future'
    elif tense_rand == 2:
        tense = 'I'
        verb['english_tense'] = 'imperfect'

    verb = conjugate(verb, tense, person, is_plural)
    # print('dat verb', verb)

    # adverb?
    if random.randint(0, 3) == 2:
        verb['modifiers'].append(adverbs[random.randint(0, len(adverbs) - 1)])

    if random.randint(0, 2) == 1:
        verb['modifiers'].append(specials['nōn'])

    return verb


def create(nominals, verbs, personal_pronouns, adverbs, adjectives, specials):
    output = {}
    person_rand = random.randint(0, 11)
    if person_rand < 2:
        output['person'] = '1'
    elif person_rand < 4:
        output['person'] = '2'
    elif person_rand < 7:
        output['person'] = '3'
        gender = 'm'
        gender_rand = random.randint(0, 3)
        if gender_rand == 1:
            gender = 'f'
        elif gender_rand == 2:
            gender = 'n'
        output['gender'] = gender
    else:
        output['person'] = 'obj'
    output['number'] = random.randint(1, 2)

    sent = []

    #subj = personal_pronouns[random.randint(0, len(personal_pronouns) - 1)]
    if output['person'] == 'obj':
        possible_subjects = filter('subj', True, nominals)
        subj = dict(possible_subjects[random.randint(0, len(possible_subjects) - 1)])
        subj = decline_noun(subj, output['number'] == 2, 'N')
        append_modifiers_to_noun(subj, adjectives)
        sent.append(subj)


    verb = dict(verbs[random.randint(0, len(verbs) - 1)])
    verb = modify_verb(output['person'], output['number'] == 2, verb, adverbs, specials)
    sent.append(verb)

    if verb['type'] == 'trans':
        obj = dict(nominals[random.randint(0, len(nominals) - 1)])
        obj = decline_noun(obj, random.randint(1, 3) == 2, 'A')
        append_modifiers_to_noun(obj, adjectives)
        sent.append(obj)

    output['sent'] = sent
    return output
