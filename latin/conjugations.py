_first_present = {
    '1-s': 'ō', '2-s': 'ās', '3-s': 'at',
    '1-p': 'āmus', '2-p': 'ātis', '3-p': 'ant'
}
_first_future = {
    '1-s': 'ābō', '2-s': 'ābis', '3-s': 'ābit',
    '1-p': 'ābimus', '2-p': 'ābitis', '3-p': 'ābunt'
}
_first_imperfect = {
    '1-s': 'ābam', '2-s': 'ābās', '3-s': 'ābat',
    '1-p': 'ābāmus', '2-p': 'ābātis', '3-p': 'ābant'
}

def _first_conjugation(word, tense, pn_key):

    form = ''
    pps = word['pp'].split('|')
    if tense == 'P':
        form = pps[0] + _first_present[pn_key]
    elif tense == 'F':
        form = pps[0] + _first_future[pn_key]
    elif tense == 'I':
        form = pps[0] + _first_imperfect[pn_key]
    else:
        print('unhandled for first conjugation', word['lex'], tense, pn_key)

    word['inflected'] = form

_second_present = {
    '1-s': 'eō', '2-s': 'ēs', '3-s': 'et',
    '1-p': 'ēmus', '2-p': 'ētis', '3-p': 'ent'
}
_second_future = {
    '1-s': 'ēbō', '2-s': 'ēbis', '3-s': 'ēbit',
    '1-p': 'ēbimus', '2-p': 'ēbitis', '3-p': 'ēbunt'
}
_second_imperfect = {
    '1-s': 'ēbam', '2-s': 'ēbās', '3-s': 'ēbat',
    '1-p': 'ēbāmus', '2-p': 'ēbātis', '3-p': 'ēbant'
}

def _second_conjugation(word, tense, pn_key):
    form = ''
    pps = word['pp'].split('|')
    if tense == 'P':
        form = pps[0] + _second_present[pn_key]
    elif tense == 'F':
        form = pps[0] + _second_future[pn_key]
    elif tense == 'I':
        form = pps[0] + _second_imperfect[pn_key]
    else:
        print('unhandled for second conjugation', word['lex'], tense, pn_key)

    word['inflected'] = form






def conjugate(word, tense, person, is_plural):
    word = dict(word)
    # print('conjugating', word['lex'], tense, person, is_plural)
    if person == 'obj':
        person = '3'

    parsing = tense + person
    if is_plural:
        parsing = parsing + 'P'
    else:
        parsing = parsing + 'S'
    word['parsing'] = parsing

    key = person + ('-p' if is_plural else '-s')

    if word['conj'] == '1':
        _first_conjugation(word, tense, key)
    elif word['conj'] == '2':
        _second_conjugation(word, tense, key)
    else:
        print('unhandled conjugation')

    return word
