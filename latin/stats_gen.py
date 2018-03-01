


def word_to_stats(word):

    if word['word-type'] == 'nominal':
        return '{lex}-{case}{gender}{number}'.format(lex=word['lex'], case=word['case'], gender=word['gender'].upper(),number=word['number'])

    return None
