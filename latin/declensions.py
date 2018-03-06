
_first_ending = {
    'N-s': 'a', 'G-s': 'ae', 'D-s': 'ae', 'A-s': 'am', 'B-s': 'ā',
    'N-p': 'ae', 'G-p': 'ārum', 'D-p': 'īs', 'A-p': 'ās', 'B-p': 'īs'
}
_second_m_ending = {
    'N-s': 'us', 'G-s': 'ī', 'D-s': 'ō', 'A-s': 'am', 'B-s': 'ō',
    'N-p': 'ī', 'G-p': 'ōrum', 'D-p': 'īs', 'A-p': 'ōs', 'B-p': 'īs'
}


def decline(word, case, is_plural, gender):
    #print('declining', word['lex'], word['stem'], word['decl'], case, is_plural, gender)

    key = case + ('-p' if is_plural else '-s')
    word['case'] = case
    word['gender'] = gender
    word['number'] = 'P' if is_plural else 'S'
    if word['decl'] == '1':
        word['inflected'] = word['stem'] + _first_ending[key]
    elif word['decl'] == '2-1-2' and gender == 'f':
        word['inflected'] = word['stem'] + _first_ending[key]
    elif word['decl'] == '2-1-2' and gender == 'm':
        word['inflected'] = word['stem'] + _second_m_ending[key]
    else:
        print('---------------- UNHANDLED DECLENSION -----------------')
