_first_a = {
    '1-s': 'ō', '2-s': 'ās', '3-s': 'at',
    '1-p': 'āmus', '2-p': 'ātis', '3-p': 'ant'
}
_first_e = {
    '1-s': 'eō', '2-s': 'ēs', '3-s': 'et',
    '1-p': 'ēmus', '2-p': 'ētis', '3-p': 'ent'
}


def conjugate(word, tense, person, is_plural):
    # print('conjugating', word['lex'], tense, person, is_plural)
    if person == 'obj':
        person = '3'

    key = person + ('-p' if is_plural else '-s')
    if word['conj'] == '1a':
        word['inflected'] = word['pp'].split('|')[0] + _first_a[key]
    elif word['conj'] == '1e':
        word['inflected'] = word['pp'].split('|')[0] + _first_e[key]
    else:
        print('unhandled conjugation')
