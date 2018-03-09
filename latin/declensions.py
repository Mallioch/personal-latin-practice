
_first_ending = {
    'N-s': 'a', 'G-s': 'ae', 'D-s': 'ae', 'A-s': 'am', 'B-s': 'ā',
    'N-p': 'ae', 'G-p': 'ārum', 'D-p': 'īs', 'A-p': 'ās', 'B-p': 'īs'
}
_second_m_ending = {
    'N-s': 'us', 'G-s': 'ī', 'D-s': 'ō', 'A-s': 'um', 'B-s': 'ō',
    'N-p': 'ī', 'G-p': 'ōrum', 'D-p': 'īs', 'A-p': 'ōs', 'B-p': 'īs'
}

def decline(word, case, is_plural, gender):
    #print('declining', word['lex'], word['stem'], word['decl'], case, is_plural, gender)
    new_word = dict(word)

    new_word['case'] = case
    new_word['gender'] = gender
    new_word['number'] = 'P' if is_plural else 'S'
    new_word['parsing'] = case + gender + new_word['number']

    if case == 'N' and new_word['word-type'] == 'nominal':
        new_word['inflected'] = new_word['lex']
        return new_word

    key = case + ('-p' if is_plural else '-s')
    if new_word['decl'] == '1':
        new_word['inflected'] = new_word['stem'] + _first_ending[key]
    elif new_word['decl'] == '2':
       new_word['inflected'] = new_word['stem'] + _second_m_ending[key]
    elif new_word['decl'] == '2-1-2' and gender == 'F':
        new_word['inflected'] = new_word['stem'] + _first_ending[key]
    elif new_word['decl'] == '2-1-2' and gender == 'M':
        new_word['inflected'] = new_word['stem'] + _second_m_ending[key]
    else:
        print(new_word['lex'])
        print('---------------- UNHANDLED DECLENSION -----------------')

    return new_word
