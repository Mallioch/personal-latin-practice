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
    { 'lex': 'annus',       'stem': 'ann',         'gender': 'M',   'decl': '2',      'subj': False, 'glosses': ['year'] },
    { 'lex': 'ager',        'stem': 'agr',         'gender': 'M',   'decl': '2',      'subj': True,  'glosses': ['field', 'farm'] },
    { 'lex': 'agricola',    'stem': 'agricol',     'gender': 'M',   'decl': '1',      'subj': True,  'glosses': ['farmer'] },
    { 'lex': 'amīcus',      'stem': 'amīc',        'gender': 'M|F', 'decl': '2',      'subj': True,  'glosses': ['friend'] },
    { 'lex': 'fāma',        'stem': 'fām',         'gender': 'F',   'decl': '1',      'subj': True,  'glosses': ['rumor', 'report', 'fame', 'reputation'] },
    { 'lex': 'fēmina',      'stem': 'fēmin',       'gender': 'F',   'decl': '1',      'subj': True,  'glosses': ['woman'] },
    { 'lex': 'fīlia',       'stem': 'fīli',        'gender': 'F',   'decl': '1',      'subj': True,  'glosses': ['daughter'] },
    { 'lex': 'fīlius',      'stem': 'fīli',        'gender': 'M',   'decl': '2',      'subj': True,  'glosses': ['son'] },
    { 'lex': 'fōrma',       'stem': 'fōrm',        'gender': 'F',   'decl': '1',      'subj': False, 'glosses': ['form', 'shape', 'beauty'] },
    { 'lex': 'fortūna',     'stem': 'fortūn',      'gender': 'F',   'decl': '1',      'subj': True,  'glosses': ['fortune', 'luck'] },
    { 'lex': 'īra',         'stem': 'īr',          'gender': 'F',   'decl': '1',      'subj': True,  'glosses': ['ire', 'anger'] },
    { 'lex': 'magister',    'stem': 'magistr',     'gender': 'M',   'decl': '2',      'subj': True,  'glosses': ['teacher'] },
    { 'lex': 'mē',          'stem': '-',           'gender': '-',   'decl': 'indecl', 'subj': False, 'glosses': ['me'] },
    { 'lex': 'nauta',       'stem': 'naut',        'gender': 'M',   'decl': '1',      'subj': True,  'glosses': ['sailor'] },
    { 'lex': 'nihil',       'stem': '-',           'gender': '-',   'decl': 'indecl', 'subj': False, 'glosses': ['nothing'] },
    { 'lex': 'numerus',     'stem': 'numeri',      'gender': 'M',   'decl': '2',      'subj': False, 'glosses': ['number'] },
    { 'lex': 'patria',      'stem': 'patri',       'gender': 'F',   'decl': '1',      'subj': True,  'glosses': ['fatherland', 'native land', 'country'] },
    { 'lex': 'pecūnia',     'stem': 'pecūni',      'gender': 'F',   'decl': '1',      'subj': True,  'glosses': ['money'] },
    { 'lex': 'philosophia', 'stem': 'philosophi',  'gender': 'F',   'decl': '1',      'subj': True,  'glosses': ['philosophy'] },
    { 'lex': 'poena',       'stem': 'poen',        'gender': 'F',   'decl': '1',      'subj': False, 'glosses': ['penalty', 'punishment'] },
    { 'lex': 'poēta',       'stem': 'poēt',        'gender': 'M',   'decl': '1',      'subj': True,  'glosses': ['poet'] },
    { 'lex': 'populus',     'stem': 'popul',       'gender': 'M',   'decl': '2',      'subj': True,  'glosses': ['people', 'nation'] },
    { 'lex': 'porta',       'stem': 'port',        'gender': 'F',   'decl': '1',      'subj': False, 'glosses': ['gate', 'entrance'] },
    { 'lex': 'puella',      'stem': 'puell',       'gender': 'F',   'decl': '1',      'subj': True,  'glosses': ['girl'] },
    { 'lex': 'puer',        'stem': 'puer',        'gender': 'M',   'decl': '2',      'subj': True,  'glosses': ['boy'] },
    { 'lex': 'rosa',        'stem': 'ros',         'gender': 'F',   'decl': '1',      'subj': False, 'glosses': ['rose'] },
    { 'lex': 'sapientia',   'stem': 'sapienti',    'gender': 'F',   'decl': '1',      'subj': True,  'glosses': ['wisdom'] },
    { 'lex': 'sententia',   'stem': 'sententi',    'gender': 'F',   'decl': '1',      'subj': False, 'glosses': ['feeling', 'thought', 'opinion', 'vote', 'sentence'] },
    { 'lex': 'vīta',        'stem': 'vīt',         'gender': 'F',   'decl': '1',      'subj': False, 'glosses': ['life', 'mode of life'] },
    { 'lex': 'vir',         'stem': 'vir',         'gender': 'M',   'decl': '2',      'subj': True,  'glosses': ['man'] },
    # { 'lex': '',       'stem': '',      'gender': '',   'decl': '2',     'subj': True,  'glosses': [] },
    # { 'lex': '',       'stem': '',      'gender': '',   'decl': '2',     'subj': True,  'glosses': [] },
    # { 'lex': '',       'stem': '',      'gender': '',   'decl': '2',     'subj': True,  'glosses': [] },
    # { 'lex': '',       'stem': '',      'gender': '',   'decl': '2',     'subj': True,  'glosses': [] },
    # { 'lex': '',       'stem': '',      'gender': '',   'decl': '2',     'subj': True,  'glosses': [] },
    # { 'lex': '',       'stem': '',      'gender': '',   'decl': '2',     'subj': True,  'glosses': [] },
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
    { 'lex': 'paucus',   'stem': 'pauc',   'decl': '2-1-2',  'glosses': ['few'] },
    { 'lex': 'Rōmānus',  'stem': 'Rōmān',  'decl': '2-1-2',  'glosses': ['Roman'] },
    { 'lex': 'stultus',  'stem': 'stult',  'decl': '2-1-2',  'glosses': ['foolish'] },
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
    {  'lex': 'accipiō',  'pp': 'accip|accip|accēp|accept', 'conj': '3', 'type': 'trans', 'glosses': ['receive', 'accept', 'get'] },
    {  'lex': 'amō',      'pp': 'am|am|am|am', 'conj': '1', 'type': 'trans', 'glosses': ['love', 'like'] },
    {  'lex': 'cōgitō',   'pp': 'cōgit|cōgit|cōgit|cōgit', 'conj': '1', 'type': 'trans', 'glosses': ['think', 'ponder', 'consider', 'plan'] },
    {  'lex': 'cōnservō', 'pp': 'cōnserv|cōnserv|cōnserv|cōnserv', 'type': 'trans', 'conj': '1', 'glosses': ['perserve', 'conserve', 'maintain'] },
    {  'lex': 'dēbeō',    'pp': 'dēb|dēb|dēbuī|dēb', 'conj': '2', 'type': 'modal', 'glosses': ['owe', 'ought', 'must', 'should'] },
    {  'lex': 'dō',       'pp': 'd|dare*|dedī*|datum*', 'conj': '1', 'type': 'trans', 'glosses': ['give', 'offer'] },
    {  'lex': 'errō',     'pp': 'err|err|err|err', 'conj': '1', 'type': 'intrans', 'glosses': ['wander', 'err', 'go astray', 'make a mistake', 'be mistaken'] },
    {  'lex': 'habeō',    'pp': 'hab|hab|hab|hab', 'conj': '2', 'type': 'trans', 'glosses': ['have', 'hold', 'possess', 'consider', 'regard'] },
    {  'lex': 'laudō',    'pp': 'laud|laud|laud|laud', 'conj': '1', 'type': 'trans', 'glosses': ['praise'] },
    {  'lex': 'moneō',    'pp': 'mon|mon|monuī', 'conj': '2', 'type': 'trans', 'glosses': ['remind', 'advise', 'warn'] },
    {  'lex': 'salveō',   'pp': 'salv|salv|-|-', 'conj': '2', 'type': 'intrans', 'glosses': ['be well', 'be in good health'] },
    {  'lex': 'satiō',    'pp': 'sati|sati|sati|sati', 'conj': '1', 'type': 'intrans', 'glosses': ['satisfy', 'sate'] },
    {  'lex': 'servō',    'pp': 'serv|serv|serv|serv', 'conj': '1', 'type': 'trans', 'glosses': ['preserver', 'save', 'keep', 'guard'] },
    {  'lex': 'terreō',   'pp': 'terr|terr|terr|terr|', 'conj': '2', 'type': 'trans', 'glosses': ['frighten', 'terrify'] },
    {  'lex': 'valeō',    'pp': 'val|val|val|valitūrum', 'conj': '2', 'type': 'intrans', 'glosses': ['be strong', 'have power', 'be well'] },
    {  'lex': 'videō',    'pp': 'vid|vid|vīdī|vīsum', 'conj': '2', 'type': 'trans', 'glosses': ['see', 'observer', 'understand'] },
    {  'lex': 'vocō',     'pp': 'voc|voc|voc|voc', 'conj': '1', 'type': 'trans', 'glosses': ['call', 'summon'] },
    {  'lex': 'doceo',    'pp': 'doc|disc|didic|-', 'conj': '3', 'type': 'trans', 'glosses': ['teach'] },
    # {  'lex': '', 'pp': '', 'conj': '1', 'type': 'trans', 'glosses': [''] },
    # {  'lex': '', 'pp': '', 'conj': '1', 'type': 'trans', 'glosses': [''] },
    # {  'lex': '', 'pp': '', 'conj': '1', 'type': 'trans', 'glosses': [''] },
    # {  'lex': '', 'pp': '', 'conj': '1', 'type': 'trans', 'glosses': [''] },
    # {  'lex': '', 'pp': '', 'conj': '1', 'type': 'trans', 'glosses': [''] },
    # {  'lex': '', 'pp': '', 'conj': '1', 'type': 'trans', 'glosses': [''] },
#    {  'lex': '', 'pp': '', 'conj': '1', 'type': 'trans', 'glosses': [''] },
# trans, intrans, modal
]

def verbs():
    return mark(_verbs, 'verb')

_adverbs = [
    { 'lex': 'atque', 'glosses': ['and', 'and also', 'and even'] },
    { 'lex': 'dum', 'glosses': ['while', 'as long as'] },
    { 'lex': 'enim', 'glosses': ['for', 'indeed', 'in truth'] },
    { 'lex': 'etiam', 'glosses': ['besides', 'also', 'even'] },
    { 'lex': 'hodiē',  'glosses': ['today'] },
    { 'lex': 'iam', 'glosses': ['now', 'already', 'soon'] },
    { 'lex': 'mox', 'glosses': ['soon'] },
    { 'lex': 'neque', 'glosses': ['and not'] },
    { 'lex': 'saepe',  'glosses': ['often'] },
    { 'lex': 'semper', 'glosses': ['always'] },
    { 'lex': 'statim', 'glosses': ['immediately', 'on the spot', 'at once'] },
    { 'lex': 'tum', 'glosses': ['then', 'at that time'] },
    { 'lex': 'tandem', 'glosses': ['finally', 'at last'] },
    { 'lex': 'ubi', 'glosses': ['where', 'when'] },
]

def adverbs():
    return mark(_adverbs, 'adv')

_specials = {
    'cōtīdiē': { 'word-type': 'adv', 'lex': 'cōtīdiē', 'glosses': ['daily'] },
    'nōn': { 'word-type': 'adv',  'lex': 'nōn', 'glosses': ['not'] },
    'at': { 'word-type': 'conj', 'lex': 'at', 'glosses': ['but'] },
    'tamen': { 'word-type': 'conj', 'lex': 'tamen', 'glosses': ['nevertheless', 'however'] },
    'sed': { 'word-type': 'conj', 'lex': 'sed', 'glosses': ['but', 'moreover', 'however'] },
    'autem': { 'word-type': 'conj', 'glosses': ['however', 'moreover'] },
}

def specials():
    return _specials

_prepositions = {
    'ā': { 'glosses': ['away from', 'out of'] },
    'ad': { 'glosses': ['to', 'toward', 'near'] },
    'ē': { 'glosses': ['out from', 'from', 'out of'], 'alt_forms': ['ex'] },
    'per': { 'glosses': ['through', 'over', 'across'] }
}

def prepositions():
    return mark(_prepositions, 'prep')
