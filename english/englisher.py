
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
            elif construct['gender'] == 'M':
                pronoun = 'he'
            elif construct['gender'] == 'F':
                pronoun = 'she'
            elif construct['gender'] == 'N':
                pronoun = 'it'
    return pronoun
