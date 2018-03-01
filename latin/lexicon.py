# Unhandled words
# ## Ch 1
# si
# valē
# ## Ch 2
# poenās dare
# et
# sed
# Ō
# sine
# est
# ## Ch 3
# de
# in

def mark(arr, name):
    output = []
    for x in arr:
        x['word-type'] = name
        output.append(x)
    return output

_nominals = [
    { 'lex': 'mē',          'stem': '-',           'gender': '-',   'decl': 'indecl', 'subj': False, 'glosses': ['me'] },
    { 'lex': 'nihil',       'stem': '-',           'gender': '-',   'decl': 'indecl', 'subj': False, 'glosses': ['nothing'] },
    { 'lex': 'fāma',        'stem': 'fām',         'gender': 'f',   'decl': '1',      'subj': True,  'glosses': ['rumor', 'report', 'fame', 'reputation'] },
    { 'lex': 'fōrma',       'stem': 'fōrm',        'gender': 'f',   'decl': '1',      'subj': False, 'glosses': ['form', 'shape', 'beauty'] },
    { 'lex': 'fortūna',     'stem': 'fortūn',      'gender': 'f',   'decl': '1',      'subj': True,  'glosses': ['fortune', 'luck'] },
    { 'lex': 'īra',         'stem': 'īr',          'gender': 'f',   'decl': '1',      'subj': True,  'glosses': ['ire', 'anger'] },
    { 'lex': 'nauta',       'stem': 'naut',        'gender': 'm',   'decl': '1',      'subj': True,  'glosses': ['sailor'] },
    { 'lex': 'patria',      'stem': 'patri',       'gender': 'f',   'decl': '1',      'subj': True,  'glosses': ['fatherland', 'native land', 'country'] },
    { 'lex': 'pecūnia',     'stem': 'pecūni',      'gender': 'f',   'decl': '1',      'subj': True,  'glosses': ['money'] },
    { 'lex': 'philosophia', 'stem': 'philosophi',  'gender': 'f',   'decl': '1',      'subj': True,  'glosses': ['philosophy'] },
    { 'lex': 'poena',       'stem': 'poen',        'gender': 'f',   'decl': '1',      'subj': False, 'glosses': ['penalty', 'punishment'] },
    { 'lex': 'poēta',       'stem': 'poēt',        'gender': 'm',   'decl': '1',      'subj': True,  'glosses': ['poet'] },
    { 'lex': 'porta',       'stem': 'port',        'gender': 'f',   'decl': '1',      'subj': False, 'glosses': ['gate', 'entrance'] },
    { 'lex': 'puella',      'stem': 'puell',       'gender': 'f',   'decl': '1',      'subj': True,  'glosses': ['girl'] },
    { 'lex': 'rosa',        'stem': 'ros',         'gender': 'f',   'decl': '1',      'subj': False, 'glosses': ['rose'] },
    { 'lex': 'sententia',   'stem': 'sententi',    'gender': 'f',   'decl': '1',      'subj': False, 'glosses': ['feeling', 'thought', 'opinion', 'vote', 'sentence'] },
    { 'lex': 'vīta',        'stem': 'vīt',         'gender': 'f',   'decl': '1',      'subj': False, 'glosses': ['life', 'mode of life'] },
    { 'lex': 'ager',        'stem': 'agr',         'gender': 'm',   'decl': '2',      'subj': True,  'glosses': ['field', 'farm'] },
    { 'lex': 'agricola',    'stem': 'agricol',     'gender': 'm',   'decl': '1',      'subj': True,  'glosses': ['farmer'] },
    { 'lex': 'amīcus',      'stem': 'amīc',        'gender': 'm|f', 'decl': '2',      'subj': True,  'glosses': ['friend'] },
    { 'lex': 'fēmina',      'stem': 'fēmin',       'gender': 'f',   'decl': '1',      'subj': True,  'glosses': ['woman'] },
    { 'lex': 'fīlia',       'stem': 'fīli',        'gender': 'f',   'decl': '1',      'subj': True,  'glosses': ['daughter'] },
    { 'lex': 'fīlius',      'stem': 'fīli',        'gender': 'm',   'decl': '2',      'subj': True,  'glosses': ['son'] },
    { 'lex': 'numerus',     'stem': 'numeri',      'gender': 'm',   'decl': '2',      'subj': False, 'glosses': ['number'] },
    { 'lex': 'populus',     'stem': 'popul',       'gender': 'm',   'decl': '2',      'subj': True,  'glosses': ['people', 'nation'] },
    { 'lex': 'puer',        'stem': 'puer',        'gender': 'm',   'decl': '2',      'subj': True,  'glosses': ['boy'] },
    { 'lex': 'sapientia',   'stem': 'sapienti',    'gender': 'f',   'decl': '1',      'subj': True,  'glosses': ['wisdom'] },
    { 'lex': 'vir',         'stem': 'vir',         'gender': 'm',   'decl': '2',      'subj': True,  'glosses': ['man'] },
    # { 'lex': '',       'stem': '',      'gender': '',   'decl': '2',     'subj': True,  'glosses': [] },
]

def nominals():
    return mark(_nominals, 'nominal')


_adjectives = [
    { 'lex': 'antīquus', 'stem': 'antīqu', 'decl': '2-1-2',  'glosses': ['ancient', 'old-time'] },
    { 'lex': 'magnus',   'stem': 'magn',   'decl': '2-1-2',  'glosses': ['large', 'great', 'important'] },
    { 'lex': 'meus',     'stem': 'me',     'decl': '2-1-2',  'glosses': ['my'] },
    { 'lex': 'multus',   'stem': 'mult',   'decl': '2-1-2',  'glosses': ['much', 'many'] },
    { 'lex': 'tuus',     'stem': 'tu',     'decl': '2-1-2',  'glosses': ['your'] },
    { 'lex': 'avārus',   'stem': 'avār',   'decl': '2-1-2',  'glosses': ['greedy', 'avaricious'] },
    { 'lex': 'pauc',     'stem': 'pauc',   'decl': '2-1-2',  'glosses': ['few'] },
    { 'lex': 'Rōmānus',  'stem': 'Rōmān',  'decl': '2-1-2',  'glosses': ['Roman'] },
#     { 'lex': '', 'stem': '',   'decl': '2-1-2',  'glosses': [] },
]

def adjectives():
    return mark(_adjectives, 'adj')


_personal_pronouns = [
    { 'lex': 'egō',  'decl': 'irreg', 'glosses': ['I'], 'forms': ['ego', 'meī', 'mihi', 'mē', 'mē', 'nōs', 'nostrum|nostrī', 'nōbīs', 'nōs', 'nōbīs'] },
    { 'lex': 'tu',  'decl': 'irreg', 'glosses': ['you'], 'forms': ['tu', 'tuī', 'tibi', 'tē', 'tē', 'vōs', 'vestrum|vestrī', 'vōbīs', 'vōs', 'vōbīs'] },
    { 'lex': 'is',  'decl': 'irreg', 'glosses': ['he'], 'forms': ['is', 'eius', 'eī', 'eum', 'eō', 'eī|iī', 'eōrum', 'eīs', 'eōs', 'eīs'] },
    { 'lex': 'id',  'decl': 'irreg', 'glosses': ['she'], 'forms': ['ea', 'eius', 'eī', 'eam', 'eā', 'eae', 'eārum', 'eīs', 'eās', 'eīs'] },
    { 'lex': 'id',  'decl': 'irreg', 'glosses': ['it'], 'forms': ['id', 'eius', 'eī', 'id', 'eō', 'ea', 'eōrum', 'eīs', 'ea', 'eīs'] },
]

def personal_pronouns():
    return mark(_personal_pronouns, 'pp')

_verbs = [
    {  'lex': 'amō', 'pp': 'am|am|am|am', 'conj': '1a', 'type': 'trans', 'glosses': ['love', 'like'] },
    {  'lex': 'cōgitō', 'pp': 'cōgit|cōgit|cōgit|cōgit', 'conj': '1a', 'type': 'trans', 'glosses': ['think', 'ponder', 'consider', 'plan'] },
    {  'lex': 'dēbeō', 'pp': 'dēb|dēb|dēbuī|dēb', 'conj': '1e', 'type': 'modal', 'glosses': ['owe', 'ought', 'must', 'should'] },
    {  'lex': 'dō', 'pp': 'd|dare*|dedī*|datum*', 'conj': '1a', 'type': 'trans', 'glosses': ['give', 'offer'] },
    {  'lex': 'errō', 'pp': 'err|err|err|err', 'conj': '1a', 'type': 'intrans', 'glosses': ['wander', 'err', 'go astray', 'make a mistake', 'be mistaken'] },
    {  'lex': 'laudō', 'pp': 'laud|laud|laud|laud', 'conj': '1a', 'type': 'trans', 'glosses': ['praise'] },
    {  'lex': 'moneō', 'pp': 'mon|mon|monuī', 'conj': '1e', 'type': 'trans', 'glosses': ['remind', 'advise', 'warn'] },
    {  'lex': 'salveō', 'pp': 'salv|salv|-|-', 'conj': '1e', 'type': 'intrans', 'glosses': ['be well', 'be in good health'] },
    {  'lex': 'servō', 'pp': 'serv|serv|serv|serv', 'conj': '1a', 'type': 'trans', 'glosses': ['preserver', 'save', 'keep', 'guard'] },
    {  'lex': 'cōnservō', 'pp': 'cōnserv|cōnserv|cōnserv|cōnserv', 'type': 'trans', 'conj': '1a', 'glosses': ['perserve', 'conserve', 'maintain'] },
    {  'lex': 'terreō', 'pp': 'terr|terr|terr|terr|', 'conj': '1e', 'type': 'trans', 'glosses': ['frighten', 'terrify'] },
    {  'lex': 'valeō', 'pp': 'val|val|val|valitūrum', 'conj': '1e', 'type': 'intrans', 'glosses': ['be strong', 'have power', 'be well'] },
    {  'lex': 'videō', 'pp': 'vid|vid|vīdī|vīsum', 'conj': '1e', 'type': 'trans', 'glosses': ['see', 'observer', 'understand'] },
    {  'lex': 'vocō', 'pp': 'voc|voc|voc|voc', 'conj': '1a', 'type': 'trans', 'glosses': ['call', 'summon'] },
    {  'lex': 'habeō', 'pp': 'hab|hab|hab|hab', 'conj': '1e', 'type': 'trans', 'glosses': ['have', 'hold', 'possess', 'consider', 'regard'] },
    {  'lex': 'satiō', 'pp': 'sati|sati|sati|sati', 'conj': '1a', 'type': 'intrans', 'glosses': ['satisfy', 'sate'] },
#    {  'lex': '', 'pp': '', 'conj': '1', 'type': 'trans', 'glosses': [''] },
# trans, intrans, modal
]

def verbs():
    return mark(_verbs, 'verb')

_adverbs = [
    {  'lex': 'saepe',  'glosses': ['often'] },
    {  'lex': 'hodiē',  'glosses': ['today'] },
    {  'lex': 'semper', 'glosses': ['always'] },
]

def adverbs():
    return mark(_adverbs, 'adv')

_specials = {
    'nōn': { 'word-type': 'adv',  'lex': 'nōn', 'glosses': ['not'] },
}

def specials():
    return _specials
