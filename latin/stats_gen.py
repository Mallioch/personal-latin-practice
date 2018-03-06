


def word_to_stats(word):

    if word['word-type'] == 'nominal':
        return '{lex}-N-{case}{gender}{number}'.format(lex=word['lex'], case=word['case'], gender=word['gender'].upper(),number=word['number'])
    if word['word-type'] == 'adj':
        return '{lex}-A-{case}{gender}{number}'.format(lex=word['lex'], case=word['case'], gender=word['gender'].upper(),number=word['number'])

    return None
