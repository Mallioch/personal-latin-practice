
def pronoun(construct):
    pronoun = ''
    if construct['person'] != 'obj':
        pronoun = 'I'
        if construct['person'] == '1' and construct['number'] == '2':
            pronoun = 'We'
        elif construct['person'] == '2':
            pronoun = 'You'
        elif construct['person'] == '3':
            if construct['number'] == '2':
                pronoun = 'they'
            elif construct['gender'] == 'm':
                pronoun = 'he'
            elif construct['gender'] == 'f':
                pronoun = 'she'
            elif construct['gender'] == 'n':
                pronoun = 'it'
    return pronoun
