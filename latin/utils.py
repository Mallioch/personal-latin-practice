def find_by_lex(words, lex):
    for item in words:
        if item['lex'] == lex:
            return item
