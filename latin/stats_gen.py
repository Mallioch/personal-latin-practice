


def word_to_stats(word):

    if word['word-type'] == 'nominal':
        return '{lex}-N-{case}{gender}{number}'.format(lex=word['lex'], case=word['case'], gender=word['gender'].upper(),number=word['number'])
    elif word['word-type'] == 'adj':
        return '{lex}-A-{case}{gender}{number}'.format(lex=word['lex'], case=word['case'], gender=word['gender'].upper(),number=word['number'])
    elif word['word-type'] == 'verb':
        return '{lex}-{parsing}'.format(lex=word['lex'], parsing=word['parsing'])

    return None
