from config.common import (
    Config,
    GotoCellDescriptor,
    TokenDesctiptor,
    make_finish_action,
    make_reduce_action,
    make_shift_action,
)

ROWS = (
    'DOWN',
    'MAIN',
    'LOADLIST',
    'LOAD1',
    'load',
    'ACTIONLIST',
    'ACTION1',
    'SET',
    'PLAY',
    'COMMON_PHRASE1',
    'CHOICE',
    'CONDITION',
    'JUMP1',
    'MARK',
    'LOADSCENE',
    'set',
    'play',
    'PHRASE_NO_OPTIONS1',
    'PHRASE1',
    'choice',
    'if',
    'jump',
    'mark',
    'load_scene',
    'label1',
    'LOADLIST`1',
    'LOAD2',
    'WHLOAD',
    'character',
    'image',
    'sound1',
    'ACTIONLIST`1',
    'ACTION2',
    'WHSET',
    'background',
    'text',
    'blackout',
    'WHPLAY',
    'sound2',
    'COMMON_PHRASE2',
    'PHRASE_NO_OPTIONS2',
    'PHRASE2',
    'label2',
    'PREDICATE1',
    'flag_name1',
    'counter_name1',
    'COMB_PRED',
    'NOT_PRED',
    'not',
    'mark_name1',
    'mark_name2',
    'path1',
    'colon1',
    'OPTIONS1',
    'open_bracket',
    'LOADLIST`2',
    'word1',
    'path2',
    'path3',
    'ACTIONLIST`2',
    'word2',
    'TexT1',
    'word3',
    'VARIANTLIST',
    'VARIANT1',
    'tab',
    'colon2',
    'OPTIONS2',
    'JUMP2',
    'bool_op',
    'is',
    'comparator_op',
    'PREDICATE2',
    'TexT2',
    'colon3',
    'position',
    'emotion1',
    'colon4',
    'VARIANTLIST`',
    'VARIANT2',
    'TexT3',
    'TexT4',
    'colon5',
    'PREDICATE3',
    'bool1',
    'digit1',
    'TexT5',
    'comma1',
    'close_bracket1',
    'close_bracket2',
    'label3',
    'colon6',
    'VARIANT3',
    'TexT6',
    'emotion2',
    'EFFECTLIST',
    'EFFECT1',
    'counter_name2',
    'flag_name2',
    'close_bracket3',
    'comma2',
    'digit_op1',
    'equals1',
    'EFFECT2',
    'counter_name3',
    'flag_name3',
    'digit2',
    'bool2',
    'digit_op2',
    'equals2',
    'digit3',
    'bool3',
)
COLS_ACTION = (
    'load',
    'character',
    'word',
    'colon',
    'label',
    'image',
    'play',
    'sound',
    'set',
    'background',
    'text',
    'TexT',
    'blackout',
    'play',
    'open_bracket',
    'position',
    'comma',
    'emotion',
    'close_bracket',
    'choice',
    'tab',
    'counter_name',
    'digit_op',
    'digit',
    'flag_name',
    'equals',
    'bool',
    'if',
    'is',
    'comparator_op',
    'bool_op',
    'not',
    'jump',
    'mark_name',
    'mark',
    'load_scene',
    'eof',
)
COLS_GOTO = (
    'S`',
    'MAIN',
    'LOADLIST',
    'LOADLIST`',
    'LOAD',
    'WHLOAD',
    'ACTIONLIST',
    'ACTIONLIST`',
    'ACTION',
    'SET',
    'WHSET',
    'PLAY',
    'WHPLAY',
    'COMMON_PHRASE',
    'PHRASE_NO_OPTIONS',
    'PHRASE',
    'OPTIONS',
    'CHOICE',
    'VARIANTLIST',
    'VARIANTLIST`',
    'VARIANT',
    'EFFECTLIST',
    'EFFECT',
    'CONDITION',
    'PREDICATE',
    'COMBINATION_PREDICATE',
    'NOT_PREDICATE',
    'JUMP',
    'MARK',
    'LOADSCENE',
)


def prepare_result(LL, AL, e):
    return {
        'res': {
            'chars': LL.get('chars'),
            'files': LL.get('files'),
            'actions': AL.get('list'),
        }
    }


def create_loadlist(L):
    return {
        'chars': [L.get('char')],
        'files': [L.get('file')],
    }


def update_loadlist(L, LL):
    return {
        'chars': [*LL.get('chars'), L.get('char')],
        'files': [*LL.get('files'), L.get('file')],
    }


def create_loadlist_b(L):
    return {
        'chars': [L.get('char')],
        'files': [L.get('file')],
    }


def update_loadlist_b(L, LL):
    return {
        'chars': [*LL.get('chars'), L.get('char')],
        'files': [*LL.get('files'), L.get('file')],
    }


def create_load(l, W):
    return {
        'char': W.get('char'),
        'file': W.get('file'),
    }


def create_load_character(c, n, s, l):
    return {'char': {'name': n.get('val'), 'label': l.get('val')}}


def create_load_image(i, p):
    return {'file': {'type': 'image', 'path': p.get('val')}}


def create_load_sound(s, p):
    return {'file': {'type': 'sound', 'path': p.get('val')}}


def create_actionlist(A):
    return {'list': [A.attributes]}


def update_actionlist(A, AL):
    return {'list': [*AL.get('list'), A.attributes]}


def create_actionlist_b(A):
    return {'list': [A.attributes]}


def update_actionlist_b(A, AL):
    return {'list': [*AL.get('list'), A.attributes]}


def wrap_set(S):
    return {
        'type': 'set_smth',
        'action': S.get('set'),
    }


def wrap_play(P):
    return {
        'type': 'play_smth',
        'action': P.get('play'),
    }


def wrap_common_phrase(C):
    return {
        'type': 'show_phrase',
        'action': C.get('phrase'),
    }


def wrap_choice(C):
    return {
        'type': 'show_choice',
        'action': C.get('choice'),
    }


def wrap_condition(C):
    return {
        'type': 'show_varle',
        'action': C.get('varle'),
    }


def wrap_jump(J):
    return {
        'type': 'jump_mark',
        'action': J.get('jump'),
    }


def wrap_mark(M):
    return {
        'type': 'create_mark',
        'action': M.get('mark'),
    }


def wrap_loadscene(L):
    return {
        'type': 'load_scene',
        'action': L.get('next_scene'),
    }


def create_set(s, W):
    return {'set': {'type': W.get('type'), 'payload': W.get('info')}}


def create_set_background(b, n):
    return {
        'type': 'set_background',
        'info': n.get('val'),
    }


def create_set_text(t, w):
    return {
        'type': 'set_text',
        'info': w.get('val'),
    }


def create_set_blackout(b):
    return {'type': 'set_blackout'}


def create_play(p, W):
    return {'play': {'type': W.get('type'), 'payload': W.get('info')}}


def create_play_sound(s, n):
    return {
        'type': 'play_sound',
        'info': n.get('val'),
    }


def wrap_phrase_no_options(P):
    return {'phrase': P.get('phrase')}


def wrap_phrase(P):
    return {'phrase': P.get('phrase')}


def create_phrase_without_options(l, s, w):
    return {
        'phrase': {
            'speaker': l.get('val'),
            'text': w.get('val'),
        }
    }


def create_phrase(l, O, s, w):
    return {
        'phrase': {
            'speaker': l.get('val'),
            'options': O.get('options'),
            'text': w.get('val'),
        }
    }


def create_options_position_and_emotion(o, p, c, e, cl):
    return {'opt': {'pos': p.get('val'), 'emo': e.get('val')}}


def create_options_emotion(o, e, c):
    return {'opt': {'pos': None, 'emo': e.get('val')}}


def create_options_position(o, p, c):
    return {'opt': {'pos': p.get('val'), 'emo': None}}


def create_choice(c, P, V):
    return {'choice': {'question': P.get('phrase'), 'variants': V.get('list')}}


def create_variant_list(V):
    return {'list': [V.get('variant')]}


def update_variant_list(V, VL):
    return {'list': [*VL.get('list'), V.get('variant')]}


def create_variant_list_b(V):
    return {'list': [V.get('variant')]}


def update_variant_list_b(V, VL):
    return {'list': [*VL.get('list'), V.get('variant')]}


def create_variant(t, w, s, EL):
    return {'variant': {'text': w.get('val'), 'effects': EL.get('list')}}


def create_effect_list(E):
    return {'list': [E.get('effect')]}


def update_effect_list(EL, c, E):
    return {'list': [*EL.get('list'), E.get('effect')]}


def create_effect_counter(cn, op, d):
    return {'effect': {'change_counter', cn.get('val'), op.get('val'), d.get('val')}}


def create_effect_flag(f, e, b):
    return {'effect': {'set_flag', f.get('val'), b.get('val')}}


def create_condition(i, P, J):
    return {'varle': {'condition': P.get('boollist'), 'target': J.get('jump')}}


def create_condition_flag(f, i, b):
    return {
        'boollist': {
            'type': 'check_flag',
            'left': f.get('val'),
            'op': 'is',
            'right': b.get('val'),
        }
    }


def create_condition_counter(cn, co, d):
    return {
        'boollist': {
            'type': 'check_counter',
            'left': cn.get('val'),
            'op': co.get('val'),
            'right': d.get('val'),
        }
    }


def wrap_comb_predicate(CP):
    return {'boollist': CP.get('boollist')}


def create_comb_predicate(C1, o, C2):
    return {
        'boollist': {
            {
                'left': C1.get('boollist'),
                'op': o.get('val'),
                'right': C2.get('boollist'),
            }
        }
    }


def wrap_not_predicate(NP):
    return {'boollist': NP.get('boollist')}


def create_not_predicate(n, C):
    return {
        'boollist': {
            {
                'left': None,
                'op': 'not',
                'right': C.get('boollist'),
            }
        }
    }


def create_jump(j, mn):
    return {'jump': {'markName': mn.get('val')}}


def create_mark(m, mn):
    return {'mark': {'markName': mn.get('val')}}


def create_load_scene(l, p):
    return {'next_scene': {'pathScene': p.get('val')}}


def make_action_table():
    action_table = dict()
    for row in ROWS:
        action_table[row] = dict({k: None for k in COLS_ACTION})

    action_table['DOWN']['load'] = make_shift_action(from_state='load', to_state='load')

    action_table['MAIN']['eof'] = make_finish_action(from_state='eof')

    action_table['LOADLIST']['label'] = make_shift_action(from_state='label', to_state='label1')
    action_table['LOADLIST']['set'] = make_shift_action(from_state='set', to_state='set')
    action_table['LOADLIST']['play'] = make_shift_action(from_state='play', to_state='play')
    action_table['LOADLIST']['choice'] = make_shift_action(from_state='choice', to_state='choice')
    action_table['LOADLIST']['if'] = make_shift_action(from_state='if', to_state='if')
    action_table['LOADLIST']['jump'] = make_shift_action(from_state='jump', to_state='jump')
    action_table['LOADLIST']['mark'] = make_shift_action(from_state='mark', to_state='mark')
    action_table['LOADLIST']['load_scene'] = make_shift_action(from_state='load_scene', to_state='load_scene')

    action_table['LOAD1']['load'] = make_shift_action(from_state='load', to_state='load')
    action_table['LOAD1']['label'] = make_reduce_action(from_state='label', to_state='LOADLIST', func=create_loadlist,)
    action_table['LOAD1']['set'] = make_reduce_action(from_state='label', to_state='LOADLIST', func=create_loadlist,)
    action_table['LOAD1']['play'] = make_reduce_action(from_state='label', to_state='LOADLIST', func=create_loadlist,)
    action_table['LOAD1']['choice'] = make_reduce_action(from_state='label', to_state='LOADLIST', func=create_loadlist,)
    action_table['LOAD1']['if'] = make_reduce_action(from_state='label', to_state='LOADLIST', func=create_loadlist,)
    action_table['LOAD1']['jump'] = make_reduce_action(from_state='label', to_state='LOADLIST', func=create_loadlist,)
    action_table['LOAD1']['mark'] = make_reduce_action(from_state='label', to_state='LOADLIST', func=create_loadlist,)
    action_table['LOAD1']['load_scene'] = make_reduce_action(
        from_state='label', to_state='LOADLIST', func=create_loadlist,
    )

    action_table['load']['character'] = make_shift_action(from_state='character', to_state='character')
    action_table['load']['image'] = make_shift_action(from_state='image', to_state='image')
    action_table['load']['sound'] = make_shift_action(from_state='sound', to_state='sound1')

    action_table['ACTIONLIST']['eof'] = make_reduce_action(from_state='eof', to_state='MAIN', func=prepare_result)

    action_table['ACTION1']['label'] = make_shift_action(from_state='label', to_state='label1')
    action_table['ACTION1']['set'] = make_shift_action(from_state='set', to_state='set')
    action_table['ACTION1']['play'] = make_shift_action(from_state='play', to_state='play')
    action_table['ACTION1']['choice'] = make_shift_action(from_state='choice', to_state='choice')
    action_table['ACTION1']['if'] = make_shift_action(from_state='if', to_state='if')
    action_table['ACTION1']['jump'] = make_shift_action(from_state='jump', to_state='jump')
    action_table['ACTION1']['mark'] = make_shift_action(from_state='mark', to_state='mark')
    action_table['ACTION1']['load_scene'] = make_shift_action(from_state='load_scene', to_state='load_scene')
    action_table['ACTION1']['eof'] = make_reduce_action(from_state='eof', to_state='ACTIONLIST', func=create_actionlist)

    action_table['SET']['label'] = make_reduce_action(from_state='label', to_state='ACTION', func=wrap_set)
    action_table['SET']['set'] = make_reduce_action(from_state='set', to_state='ACTION', func=wrap_set)
    action_table['SET']['play'] = make_reduce_action(from_state='play', to_state='ACTION', func=wrap_set)
    action_table['SET']['choice'] = make_reduce_action(from_state='choice', to_state='ACTION', func=wrap_set)
    action_table['SET']['if'] = make_reduce_action(from_state='if', to_state='ACTION', func=wrap_set)
    action_table['SET']['jump'] = make_reduce_action(from_state='jump', to_state='ACTION', func=wrap_set)
    action_table['SET']['mark'] = make_reduce_action(from_state='mark', to_state='ACTION', func=wrap_set)
    action_table['SET']['load_scene'] = make_reduce_action(from_state='load_scene', to_state='ACTION', func=wrap_set)
    action_table['SET']['eof'] = make_reduce_action(from_state='load_scene', to_state='ACTION', func=wrap_set)

    action_table['PLAY']['label'] = make_reduce_action(from_state='label', to_state='ACTION', func=wrap_play)
    action_table['PLAY']['set'] = make_reduce_action(from_state='set', to_state='ACTION', func=wrap_play)
    action_table['PLAY']['play'] = make_reduce_action(from_state='play', to_state='ACTION', func=wrap_play)
    action_table['PLAY']['choice'] = make_reduce_action(from_state='choice', to_state='ACTION', func=wrap_play)
    action_table['PLAY']['if'] = make_reduce_action(from_state='if', to_state='ACTION', func=wrap_play)
    action_table['PLAY']['jump'] = make_reduce_action(from_state='jump', to_state='ACTION', func=wrap_play)
    action_table['PLAY']['mark'] = make_reduce_action(from_state='mark', to_state='ACTION', func=wrap_play)
    action_table['PLAY']['load_scene'] = make_reduce_action(from_state='load_scene', to_state='ACTION', func=wrap_play)
    action_table['PLAY']['eof'] = make_reduce_action(from_state='load_scene', to_state='ACTION', func=wrap_play)

    action_table['COMMON_PHRASE1']['label'] = make_reduce_action(
        from_state='label', to_state='ACTION', func=wrap_common_phrase
    )
    action_table['COMMON_PHRASE1']['set'] = make_reduce_action(
        from_state='set', to_state='ACTION', func=wrap_common_phrase
    )
    action_table['COMMON_PHRASE1']['play'] = make_reduce_action(
        from_state='play', to_state='ACTION', func=wrap_common_phrase
    )
    action_table['COMMON_PHRASE1']['choice'] = make_reduce_action(
        from_state='choice', to_state='ACTION', func=wrap_common_phrase
    )
    action_table['COMMON_PHRASE1']['if'] = make_reduce_action(
        from_state='if', to_state='ACTION', func=wrap_common_phrase
    )
    action_table['COMMON_PHRASE1']['jump'] = make_reduce_action(
        from_state='jump', to_state='ACTION', func=wrap_common_phrase
    )
    action_table['COMMON_PHRASE1']['mark'] = make_reduce_action(
        from_state='mark', to_state='ACTION', func=wrap_common_phrase
    )
    action_table['COMMON_PHRASE1']['load_scene'] = make_reduce_action(
        from_state='load_scene', to_state='ACTION', func=wrap_common_phrase
    )
    action_table['COMMON_PHRASE1']['eof'] = make_reduce_action(
        from_state='load_scene', to_state='ACTION', func=wrap_common_phrase
    )

    action_table['CHOICE']['label'] = make_reduce_action(from_state='label', to_state='ACTION', func=wrap_choice)
    action_table['CHOICE']['set'] = make_reduce_action(from_state='set', to_state='ACTION', func=wrap_choice)
    action_table['CHOICE']['play'] = make_reduce_action(from_state='play', to_state='ACTION', func=wrap_choice)
    action_table['CHOICE']['choice'] = make_reduce_action(from_state='choice', to_state='ACTION', func=wrap_choice)
    action_table['CHOICE']['if'] = make_reduce_action(from_state='if', to_state='ACTION', func=wrap_choice)
    action_table['CHOICE']['jump'] = make_reduce_action(from_state='jump', to_state='ACTION', func=wrap_choice)
    action_table['CHOICE']['mark'] = make_reduce_action(from_state='mark', to_state='ACTION', func=wrap_choice)
    action_table['CHOICE']['load_scene'] = make_reduce_action(
        from_state='load_scene', to_state='ACTION', func=wrap_choice
    )
    action_table['CHOICE']['eof'] = make_reduce_action(from_state='load_scene', to_state='ACTION', func=wrap_choice)

    action_table['CONDITION']['label'] = make_reduce_action(from_state='label', to_state='ACTION', func=wrap_condition)
    action_table['CONDITION']['set'] = make_reduce_action(from_state='set', to_state='ACTION', func=wrap_condition)
    action_table['CONDITION']['play'] = make_reduce_action(from_state='play', to_state='ACTION', func=wrap_condition)
    action_table['CONDITION']['choice'] = make_reduce_action(
        from_state='choice', to_state='ACTION', func=wrap_condition
    )
    action_table['CONDITION']['if'] = make_reduce_action(from_state='if', to_state='ACTION', func=wrap_condition)
    action_table['CONDITION']['jump'] = make_reduce_action(from_state='jump', to_state='ACTION', func=wrap_condition)
    action_table['CONDITION']['mark'] = make_reduce_action(from_state='mark', to_state='ACTION', func=wrap_condition)
    action_table['CONDITION']['load_scene'] = make_reduce_action(
        from_state='load_scene', to_state='ACTION', func=wrap_condition
    )
    action_table['CONDITION']['eof'] = make_reduce_action(
        from_state='load_scene', to_state='ACTION', func=wrap_condition
    )

    action_table['JUMP1']['label'] = make_reduce_action(from_state='label', to_state='ACTION', func=wrap_jump)
    action_table['JUMP1']['set'] = make_reduce_action(from_state='set', to_state='ACTION', func=wrap_jump)
    action_table['JUMP1']['play'] = make_reduce_action(from_state='play', to_state='ACTION', func=wrap_jump)
    action_table['JUMP1']['choice'] = make_reduce_action(from_state='choice', to_state='ACTION', func=wrap_jump)
    action_table['JUMP1']['if'] = make_reduce_action(from_state='if', to_state='ACTION', func=wrap_jump)
    action_table['JUMP1']['jump'] = make_reduce_action(from_state='jump', to_state='ACTION', func=wrap_jump)
    action_table['JUMP1']['mark'] = make_reduce_action(from_state='mark', to_state='ACTION', func=wrap_jump)
    action_table['JUMP1']['load_scene'] = make_reduce_action(from_state='load_scene', to_state='ACTION', func=wrap_jump)
    action_table['JUMP1']['eof'] = make_reduce_action(from_state='load_scene', to_state='ACTION', func=wrap_jump)

    action_table['MARK']['label'] = make_reduce_action(from_state='label', to_state='ACTION', func=wrap_mark)
    action_table['MARK']['set'] = make_reduce_action(from_state='set', to_state='ACTION', func=wrap_mark)
    action_table['MARK']['play'] = make_reduce_action(from_state='play', to_state='ACTION', func=wrap_mark)
    action_table['MARK']['choice'] = make_reduce_action(from_state='choice', to_state='ACTION', func=wrap_mark)
    action_table['MARK']['if'] = make_reduce_action(from_state='if', to_state='ACTION', func=wrap_mark)
    action_table['MARK']['jump'] = make_reduce_action(from_state='jump', to_state='ACTION', func=wrap_mark)
    action_table['MARK']['mark'] = make_reduce_action(from_state='mark', to_state='ACTION', func=wrap_mark)
    action_table['MARK']['load_scene'] = make_reduce_action(from_state='load_scene', to_state='ACTION', func=wrap_mark)
    action_table['MARK']['eof'] = make_reduce_action(from_state='load_scene', to_state='ACTION', func=wrap_mark)

    action_table['LOADSCENE']['label'] = make_reduce_action(from_state='label', to_state='ACTION', func=wrap_loadscene)
    action_table['LOADSCENE']['set'] = make_reduce_action(from_state='set', to_state='ACTION', func=wrap_loadscene)
    action_table['LOADSCENE']['play'] = make_reduce_action(from_state='play', to_state='ACTION', func=wrap_loadscene)
    action_table['LOADSCENE']['choice'] = make_reduce_action(
        from_state='choice', to_state='ACTION', func=wrap_loadscene
    )
    action_table['LOADSCENE']['if'] = make_reduce_action(from_state='if', to_state='ACTION', func=wrap_loadscene)
    action_table['LOADSCENE']['jump'] = make_reduce_action(from_state='jump', to_state='ACTION', func=wrap_loadscene)
    action_table['LOADSCENE']['mark'] = make_reduce_action(from_state='mark', to_state='ACTION', func=wrap_loadscene)
    action_table['LOADSCENE']['load_scene'] = make_reduce_action(
        from_state='load_scene', to_state='ACTION', func=wrap_loadscene
    )
    action_table['LOADSCENE']['eof'] = make_reduce_action(
        from_state='load_scene', to_state='ACTION', func=wrap_loadscene
    )

    action_table['set']['background'] = make_shift_action(from_state='background', to_state='background')
    action_table['set']['text'] = make_shift_action(from_state='text', to_state='text')
    action_table['set']['blackout'] = make_shift_action(from_state='blackout', to_state='blackout')

    action_table['play']['sound'] = make_shift_action(from_state='sound', to_state='sound2')

    action_table['PHRASE_NO_OPTIONS1']['label'] = make_reduce_action(
        from_state='label',
        to_state='COMMON_PHRASE',
        func=wrap_phrase_no_options,
    )
    action_table['PHRASE_NO_OPTIONS1']['set'] = make_reduce_action(
        from_state='set',
        to_state='COMMON_PHRASE',
        func=wrap_phrase_no_options,
    )
    action_table['PHRASE_NO_OPTIONS1']['play'] = make_reduce_action(
        from_state='play',
        to_state='COMMON_PHRASE',
        func=wrap_phrase_no_options,
    )
    action_table['PHRASE_NO_OPTIONS1']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='COMMON_PHRASE',
        func=wrap_phrase_no_options,
    )
    action_table['PHRASE_NO_OPTIONS1']['if'] = make_reduce_action(
        from_state='if',
        to_state='COMMON_PHRASE',
        func=wrap_phrase_no_options,
    )
    action_table['PHRASE_NO_OPTIONS1']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='COMMON_PHRASE',
        func=wrap_phrase_no_options,
    )
    action_table['PHRASE_NO_OPTIONS1']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='COMMON_PHRASE',
        func=wrap_phrase_no_options,
    )
    action_table['PHRASE_NO_OPTIONS1']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='COMMON_PHRASE',
        func=wrap_phrase_no_options,
    )
    action_table['PHRASE_NO_OPTIONS1']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='COMMON_PHRASE',
        func=wrap_phrase_no_options,
    )

    action_table['PHRASE1']['label'] = make_reduce_action(
        from_state='label',
        to_state='COMMON_PHRASE',
        func=wrap_phrase,
    )
    action_table['PHRASE1']['set'] = make_reduce_action(
        from_state='set',
        to_state='COMMON_PHRASE',
        func=wrap_phrase,
    )
    action_table['PHRASE1']['play'] = make_reduce_action(
        from_state='play',
        to_state='COMMON_PHRASE',
        func=wrap_phrase,
    )
    action_table['PHRASE1']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='COMMON_PHRASE',
        func=wrap_phrase,
    )
    action_table['PHRASE1']['if'] = make_reduce_action(
        from_state='if',
        to_state='COMMON_PHRASE',
        func=wrap_phrase,
    )
    action_table['PHRASE1']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='COMMON_PHRASE',
        func=wrap_phrase,
    )
    action_table['PHRASE1']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='COMMON_PHRASE',
        func=wrap_phrase,
    )
    action_table['PHRASE1']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='COMMON_PHRASE',
        func=wrap_phrase,
    )
    action_table['PHRASE1']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='COMMON_PHRASE',
        func=wrap_phrase,
    )

    action_table['choice']['label'] = make_shift_action(from_state='label', to_state='label2')

    action_table['if']['counter_name'] = make_shift_action(from_state='counter_name', to_state='counter_name1')
    action_table['if']['flag_name'] = make_shift_action(from_state='flag_name', to_state='flag_name1')
    action_table['if']['not'] = make_shift_action(from_state='not', to_state='not')

    action_table['jump']['mark_name'] = make_shift_action(from_state='mark_name', to_state='mark_name1')

    action_table['mark']['mark_name'] = make_shift_action(from_state='mark_name', to_state='mark_name2')

    action_table['load_scene']['path'] = make_shift_action(from_state='path', to_state='path1')

    action_table['label1']['colon'] = make_shift_action(from_state='colon', to_state='colon1')
    action_table['label1']['open_bracket'] = make_shift_action(from_state='open_bracket', to_state='open_bracket')

    action_table['LOADLIST`1']['label'] = make_reduce_action(
        from_state='label',
        to_state='LOADLIST',
        func=update_loadlist,
    )
    action_table['LOADLIST`1']['set'] = make_reduce_action(
        from_state='set',
        to_state='LOADLIST',
        func=update_loadlist,
    )
    action_table['LOADLIST`1']['play'] = make_reduce_action(
        from_state='play',
        to_state='LOADLIST',
        func=update_loadlist,
    )
    action_table['LOADLIST`1']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='LOADLIST',
        func=update_loadlist,
    )
    action_table['LOADLIST`1']['if'] = make_reduce_action(
        from_state='if',
        to_state='LOADLIST',
        func=update_loadlist,
    )
    action_table['LOADLIST`1']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='LOADLIST',
        func=update_loadlist,
    )
    action_table['LOADLIST`1']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='LOADLIST',
        func=update_loadlist,
    )
    action_table['LOADLIST`1']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='LOADLIST',
        func=update_loadlist,
    )

    action_table['LOAD2']['load'] = make_shift_action(from_state='load', to_state='load')
    action_table['LOAD2']['label'] = make_reduce_action(
        from_state='label',
        to_state='LOADLIST`',
        func=create_loadlist_b,
    )
    action_table['LOAD2']['set'] = make_reduce_action(
        from_state='set',
        to_state='LOADLIST`',
        func=create_loadlist_b,
    )
    action_table['LOAD2']['play'] = make_reduce_action(
        from_state='play',
        to_state='LOADLIST`',
        func=create_loadlist_b,
    )
    action_table['LOAD2']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='LOADLIST`',
        func=create_loadlist_b,
    )
    action_table['LOAD2']['if'] = make_reduce_action(
        from_state='if',
        to_state='LOADLIST`',
        func=create_loadlist_b,
    )
    action_table['LOAD2']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='LOADLIST`',
        func=create_loadlist_b,
    )
    action_table['LOAD2']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='LOADLIST`',
        func=create_loadlist_b,
    )
    action_table['LOAD2']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='LOADLIST`',
        func=create_loadlist_b,
    )

    action_table['WHLOAD']['load'] = make_reduce_action(
        from_state='load',
        to_state='LOAD',
        func=create_load,
    )
    action_table['WHLOAD']['label'] = make_reduce_action(
        from_state='label',
        to_state='LOAD',
        func=create_load,
    )
    action_table['WHLOAD']['set'] = make_reduce_action(
        from_state='set',
        to_state='LOAD',
        func=create_load,
    )
    action_table['WHLOAD']['play'] = make_reduce_action(
        from_state='play',
        to_state='LOAD',
        func=create_load,
    )
    action_table['WHLOAD']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='LOAD',
        func=create_load,
    )
    action_table['WHLOAD']['if'] = make_reduce_action(
        from_state='if',
        to_state='LOAD',
        func=create_load,
    )
    action_table['WHLOAD']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='LOAD',
        func=create_load,
    )
    action_table['WHLOAD']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='LOAD',
        func=create_load,
    )
    action_table['WHLOAD']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='LOAD',
        func=create_load,
    )

    action_table['character']['word'] = make_shift_action(from_state='word', to_state='word1')

    action_table['image']['path'] = make_shift_action(from_state='path', to_state='path2')

    action_table['sound1']['path'] = make_shift_action(from_state='path', to_state='path3')

    action_table['ACTIONLIST`1']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='ACTIONLIST',
        func=update_actionlist,
    )

    action_table['ACTION2']['label'] = make_shift_action(from_state='label', to_state='label1')
    action_table['ACTION2']['set'] = make_shift_action(from_state='set', to_state='set')
    action_table['ACTION2']['play'] = make_shift_action(from_state='play', to_state='play')
    action_table['ACTION2']['choice'] = make_shift_action(from_state='choice', to_state='choice')
    action_table['ACTION2']['if'] = make_shift_action(from_state='if', to_state='if')
    action_table['ACTION2']['jump'] = make_shift_action(from_state='jump', to_state='jump')
    action_table['ACTION2']['mark'] = make_shift_action(from_state='mark', to_state='mark')
    action_table['ACTION2']['load_scene'] = make_shift_action(from_state='load_scene', to_state='load_scene')
    action_table['ACTION2']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='ACTIONLIST`',
        func=create_actionlist_b,
    )

    action_table['WHSET']['label'] = make_reduce_action(
        from_state='label',
        to_state='SET',
        func=create_set,
    )
    action_table['WHSET']['set'] = make_reduce_action(
        from_state='set',
        to_state='SET',
        func=create_set,
    )
    action_table['WHSET']['play'] = make_reduce_action(
        from_state='play',
        to_state='SET',
        func=create_set,
    )
    action_table['WHSET']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='SET',
        func=create_set,
    )
    action_table['WHSET']['if'] = make_reduce_action(
        from_state='if',
        to_state='SET',
        func=create_set,
    )
    action_table['WHSET']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='SET',
        func=create_set,
    )
    action_table['WHSET']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='SET',
        func=create_set,
    )
    action_table['WHSET']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='SET',
        func=create_set,
    )
    action_table['WHSET']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='SET',
        func=create_set,
    )

    action_table['blackout']['label'] = make_reduce_action(
        from_state='label',
        to_state='WHSET',
        func=create_set_blackout,
    )
    action_table['blackout']['set'] = make_reduce_action(
        from_state='set',
        to_state='WHSET',
        func=create_set_blackout,
    )
    action_table['blackout']['play'] = make_reduce_action(
        from_state='play',
        to_state='WHSET',
        func=create_set_blackout,
    )
    action_table['blackout']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='WHSET',
        func=create_set_blackout,
    )
    action_table['blackout']['if'] = make_reduce_action(
        from_state='if',
        to_state='WHSET',
        func=create_set_blackout,
    )
    action_table['blackout']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='WHSET',
        func=create_set_blackout,
    )
    action_table['blackout']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='WHSET',
        func=create_set_blackout,
    )
    action_table['blackout']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='WHSET',
        func=create_set_blackout,
    )
    action_table['blackout']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='WHSET',
        func=create_set_blackout,
    )

    action_table['WHPLAY']['label'] = make_reduce_action(
        from_state='label',
        to_state='PLAY',
        func=create_play,
    )
    action_table['WHPLAY']['set'] = make_reduce_action(
        from_state='set',
        to_state='PLAY',
        func=create_play,
    )
    action_table['WHPLAY']['play'] = make_reduce_action(
        from_state='play',
        to_state='PLAY',
        func=create_play,
    )
    action_table['WHPLAY']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='PLAY',
        func=create_play,
    )
    action_table['WHPLAY']['if'] = make_reduce_action(
        from_state='if',
        to_state='PLAY',
        func=create_play,
    )
    action_table['WHPLAY']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='PLAY',
        func=create_play,
    )
    action_table['WHPLAY']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='PLAY',
        func=create_play,
    )
    action_table['WHPLAY']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='PLAY',
        func=create_play,
    )
    action_table['WHPLAY']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='PLAY',
        func=create_play,
    )

    action_table['background']['word'] = make_shift_action(from_state='word', to_state='word2')

    action_table['text']['TexT'] = make_shift_action(from_state='TexT', to_state='TexT1')

    action_table['sound2']['word'] = make_shift_action(from_state='word', to_state='word3')

    action_table['COMMON_PHRASE2']['tab'] = make_shift_action(from_state='tab', to_state='tab')

    action_table['PHRASE_NO_OPTIONS2']['tab'] = make_reduce_action(
        from_state='tab',
        to_state='COMMON_PHRASE',
        func=wrap_phrase_no_options,
    )

    action_table['PHRASE2']['tab'] = make_reduce_action(
        from_state='tab',
        to_state='COMMON_PHRASE',
        func=wrap_phrase,
    )

    action_table['label2']['colon'] = make_shift_action(from_state='colon', to_state='colon2')
    action_table['label2']['open_bracket'] = make_shift_action(from_state='open_bracket', to_state='open_bracket')

    action_table['PREDICATE1']['bool_op'] = make_shift_action(from_state='bool_op', to_state='bool_op')
    action_table['PREDICATE1']['jump'] = make_shift_action(from_state='jump', to_state='jump')

    action_table['flag_name1']['is'] = make_shift_action(from_state='is', to_state='is')

    action_table['counter_name1']['comparator_op'] = make_shift_action(
        from_state='comparator_op', to_state='comparator_op'
    )

    action_table['COMB_PRED']['bool_op'] = make_reduce_action(
        from_state='bool_op',
        to_state='PREDICATE',
        func=wrap_comb_predicate,
    )
    action_table['COMB_PRED']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='PREDICATE',
        func=wrap_comb_predicate,
    )

    action_table['NOT_PRED']['bool_op'] = make_reduce_action(
        from_state='bool_op',
        to_state='PREDICATE',
        func=wrap_not_predicate,
    )
    action_table['NOT_PRED']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='PREDICATE',
        func=wrap_not_predicate,
    )

    action_table['not']['counter_name'] = make_shift_action(from_state='counter_name', to_state='counter_name1')
    action_table['not']['flag_name'] = make_shift_action(from_state='flag_name', to_state='flag_name1')
    action_table['not']['not'] = make_shift_action(from_state='not', to_state='not')

    action_table['mark_name1']['label'] = make_reduce_action(
        from_state='label',
        to_state='JUMP',
        func=create_jump,
    )
    action_table['mark_name1']['set'] = make_reduce_action(
        from_state='set',
        to_state='JUMP',
        func=create_jump,
    )
    action_table['mark_name1']['play'] = make_reduce_action(
        from_state='play',
        to_state='JUMP',
        func=create_jump,
    )
    action_table['mark_name1']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='JUMP',
        func=create_jump,
    )
    action_table['mark_name1']['if'] = make_reduce_action(
        from_state='if',
        to_state='JUMP',
        func=create_jump,
    )
    action_table['mark_name1']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='JUMP',
        func=create_jump,
    )
    action_table['mark_name1']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='JUMP',
        func=create_jump,
    )
    action_table['mark_name1']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='JUMP',
        func=create_jump,
    )
    action_table['mark_name1']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='JUMP',
        func=create_jump,
    )

    action_table['mark_name2']['label'] = make_reduce_action(
        from_state='label',
        to_state='MARK',
        func=create_mark,
    )
    action_table['mark_name2']['set'] = make_reduce_action(
        from_state='set',
        to_state='MARK',
        func=create_mark,
    )
    action_table['mark_name2']['play'] = make_reduce_action(
        from_state='play',
        to_state='MARK',
        func=create_mark,
    )
    action_table['mark_name2']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='MARK',
        func=create_mark,
    )
    action_table['mark_name2']['if'] = make_reduce_action(
        from_state='if',
        to_state='MARK',
        func=create_mark,
    )
    action_table['mark_name2']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='MARK',
        func=create_mark,
    )
    action_table['mark_name2']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='MARK',
        func=create_mark,
    )
    action_table['mark_name2']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='MARK',
        func=create_mark,
    )
    action_table['mark_name2']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='MARK',
        func=create_mark,
    )

    action_table['path1']['label'] = make_reduce_action(
        from_state='label',
        to_state='LOADSCENE',
        func=create_load_scene,
    )
    action_table['path1']['set'] = make_reduce_action(
        from_state='set',
        to_state='LOADSCENE',
        func=create_load_scene,
    )
    action_table['path1']['play'] = make_reduce_action(
        from_state='play',
        to_state='LOADSCENE',
        func=create_load_scene,
    )
    action_table['path1']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='LOADSCENE',
        func=create_load_scene,
    )
    action_table['path1']['if'] = make_reduce_action(
        from_state='if',
        to_state='LOADSCENE',
        func=create_load_scene,
    )
    action_table['path1']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='LOADSCENE',
        func=create_load_scene,
    )
    action_table['path1']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='LOADSCENE',
        func=create_load_scene,
    )
    action_table['path1']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='LOADSCENE',
        func=create_load_scene,
    )
    action_table['path1']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='LOADSCENE',
        func=create_load_scene,
    )

    action_table['colon1']['TexT'] = make_shift_action(from_state='TexT', to_state='TexT2')

    action_table['OPTIONS1']['colon'] = make_shift_action(from_state='colon', to_state='colon3')

    action_table['open_bracket']['position'] = make_shift_action(from_state='position', to_state='position')
    action_table['open_bracket']['emotion'] = make_shift_action(from_state='emotion', to_state='emotion1')

    action_table['LOADLIST`2']['label'] = make_reduce_action(
        from_state='label',
        to_state='LOADLIST`',
        func=update_loadlist_b,
    )
    action_table['LOADLIST`2']['set'] = make_reduce_action(
        from_state='set',
        to_state='LOADLIST`',
        func=update_loadlist_b,
    )
    action_table['LOADLIST`2']['paly'] = make_reduce_action(
        from_state='play',
        to_state='LOADLIST`',
        func=update_loadlist_b,
    )
    action_table['LOADLIST`2']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='LOADLIST`',
        func=update_loadlist_b,
    )
    action_table['LOADLIST`2']['if'] = make_reduce_action(
        from_state='if',
        to_state='LOADLIST`',
        func=update_loadlist_b,
    )
    action_table['LOADLIST`2']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='LOADLIST`',
        func=update_loadlist_b,
    )
    action_table['LOADLIST`2']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='LOADLIST`',
        func=update_loadlist_b,
    )
    action_table['LOADLIST`2']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='LOADLIST`',
        func=update_loadlist_b,
    )

    action_table['path2']['load'] = make_reduce_action(
        from_state='load',
        to_state='WHLOAD',
        func=create_load_image,
    )
    action_table['path2']['label'] = make_reduce_action(
        from_state='label',
        to_state='WHLOAD',
        func=create_load_image,
    )
    action_table['path2']['set'] = make_reduce_action(
        from_state='set',
        to_state='WHLOAD',
        func=create_load_image,
    )
    action_table['path2']['paly'] = make_reduce_action(
        from_state='play',
        to_state='WHLOAD',
        func=create_load_image,
    )
    action_table['path2']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='WHLOAD',
        func=create_load_image,
    )
    action_table['path2']['if'] = make_reduce_action(
        from_state='if',
        to_state='WHLOAD',
        func=create_load_image,
    )
    action_table['path2']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='WHLOAD',
        func=create_load_image,
    )
    action_table['path2']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='WHLOAD',
        func=create_load_image,
    )
    action_table['path2']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='WHLOAD',
        func=create_load_image,
    )

    action_table['path3']['load'] = make_reduce_action(
        from_state='load',
        to_state='WHLOAD',
        func=create_load_sound,
    )
    action_table['path3']['label'] = make_reduce_action(
        from_state='label',
        to_state='WHLOAD',
        func=create_load_sound,
    )
    action_table['path3']['set'] = make_reduce_action(
        from_state='set',
        to_state='WHLOAD',
        func=create_load_sound,
    )
    action_table['path3']['paly'] = make_reduce_action(
        from_state='play',
        to_state='WHLOAD',
        func=create_load_sound,
    )
    action_table['path3']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='WHLOAD',
        func=create_load_sound,
    )
    action_table['path3']['if'] = make_reduce_action(
        from_state='if',
        to_state='WHLOAD',
        func=create_load_sound,
    )
    action_table['path3']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='WHLOAD',
        func=create_load_sound,
    )
    action_table['path3']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='WHLOAD',
        func=create_load_sound,
    )
    action_table['path3']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='WHLOAD',
        func=create_load_sound,
    )

    action_table['word1']['colon'] = make_shift_action(from_state='colon', to_state='colon4')

    action_table['ACTIONLIST`2']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='ACTIONLIST`',
        func=update_actionlist_b,
    )

    action_table['word2']['label'] = make_reduce_action(
        from_state='label',
        to_state='WHSET',
        func=create_set_background,
    )
    action_table['word2']['set'] = make_reduce_action(
        from_state='set',
        to_state='WHSET',
        func=create_set_background,
    )
    action_table['word2']['play'] = make_reduce_action(
        from_state='play',
        to_state='WHSET',
        func=create_set_background,
    )
    action_table['word2']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='WHSET',
        func=create_set_background,
    )
    action_table['word2']['if'] = make_reduce_action(
        from_state='if',
        to_state='WHSET',
        func=create_set_background,
    )
    action_table['word2']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='WHSET',
        func=create_set_background,
    )
    action_table['word2']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='WHSET',
        func=create_set_background,
    )
    action_table['word2']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='WHSET',
        func=create_set_background,
    )
    action_table['word2']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='WHSET',
        func=create_set_background,
    )

    action_table['TexT1']['label'] = make_reduce_action(
        from_state='label',
        to_state='WHSET',
        func=create_set_text,
    )
    action_table['TexT1']['set'] = make_reduce_action(
        from_state='set',
        to_state='WHSET',
        func=create_set_text,
    )
    action_table['TexT1']['play'] = make_reduce_action(
        from_state='play',
        to_state='WHSET',
        func=create_set_text,
    )
    action_table['TexT1']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='WHSET',
        func=create_set_text,
    )
    action_table['TexT1']['if'] = make_reduce_action(
        from_state='if',
        to_state='WHSET',
        func=create_set_text,
    )
    action_table['TexT1']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='WHSET',
        func=create_set_text,
    )
    action_table['TexT1']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='WHSET',
        func=create_set_text,
    )
    action_table['TexT1']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='WHSET',
        func=create_set_text,
    )
    action_table['TexT1']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='WHSET',
        func=create_set_text,
    )

    action_table['word3']['label'] = make_reduce_action(
        from_state='label',
        to_state='WHPLAY',
        func=create_play_sound,
    )
    action_table['word3']['set'] = make_reduce_action(
        from_state='set',
        to_state='WHPLAY',
        func=create_play_sound,
    )
    action_table['word3']['play'] = make_reduce_action(
        from_state='play',
        to_state='WHPLAY',
        func=create_play_sound,
    )
    action_table['word3']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='WHPLAY',
        func=create_play_sound,
    )
    action_table['word3']['if'] = make_reduce_action(
        from_state='if',
        to_state='WHPLAY',
        func=create_play_sound,
    )
    action_table['word3']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='WHPLAY',
        func=create_play_sound,
    )
    action_table['word3']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='WHPLAY',
        func=create_play_sound,
    )
    action_table['word3']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='WHPLAY',
        func=create_play_sound,
    )
    action_table['word3']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='WHPLAY',
        func=create_play_sound,
    )

    action_table['VARIANTLIST']['label'] = make_reduce_action(
        from_state='label',
        to_state='CHOICE',
        func=create_choice,
    )
    action_table['VARIANTLIST']['set'] = make_reduce_action(
        from_state='set',
        to_state='CHOICE',
        func=create_choice,
    )
    action_table['VARIANTLIST']['play'] = make_reduce_action(
        from_state='play',
        to_state='CHOICE',
        func=create_choice,
    )
    action_table['VARIANTLIST']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='CHOICE',
        func=create_choice,
    )
    action_table['VARIANTLIST']['if'] = make_reduce_action(
        from_state='if',
        to_state='CHOICE',
        func=create_choice,
    )
    action_table['VARIANTLIST']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='CHOICE',
        func=create_choice,
    )
    action_table['VARIANTLIST']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='CHOICE',
        func=create_choice,
    )
    action_table['VARIANTLIST']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='CHOICE',
        func=create_choice,
    )
    action_table['VARIANTLIST']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='CHOICE',
        func=create_choice,
    )

    action_table['VARIANT1']['label'] = make_reduce_action(
        from_state='label',
        to_state='VARIANTLIST',
        func=create_variant_list,
    )
    action_table['VARIANT1']['set'] = make_reduce_action(
        from_state='set',
        to_state='VARIANTLIST',
        func=create_variant_list,
    )
    action_table['VARIANT1']['play'] = make_reduce_action(
        from_state='play',
        to_state='VARIANTLIST',
        func=create_variant_list,
    )
    action_table['VARIANT1']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='VARIANTLIST',
        func=create_variant_list,
    )
    action_table['VARIANT1']['tab'] = make_shift_action(from_state='tab', to_state='tab')
    action_table['VARIANT1']['if'] = make_reduce_action(
        from_state='if',
        to_state='VARIANTLIST',
        func=create_variant_list,
    )
    action_table['VARIANT1']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='VARIANTLIST',
        func=create_variant_list,
    )
    action_table['VARIANT1']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='VARIANTLIST',
        func=create_variant_list,
    )
    action_table['VARIANT1']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='VARIANTLIST',
        func=create_variant_list,
    )
    action_table['VARIANT1']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='VARIANTLIST',
        func=create_variant_list,
    )

    action_table['tab']['TexT'] = make_shift_action(from_state='TexT', to_state='TexT3')

    action_table['colon2']['TexT'] = make_shift_action(from_state='TexT', to_state='TexT4')

    action_table['OPTIONS2']['colon'] = make_shift_action(from_state='colon', to_state='colon5')

    action_table['JUMP2']['label'] = make_reduce_action(
        from_state='label',
        to_state='CONDITION',
        func=create_condition,
    )
    action_table['JUMP2']['set'] = make_reduce_action(
        from_state='set',
        to_state='CONDITION',
        func=create_condition,
    )
    action_table['JUMP2']['play'] = make_reduce_action(
        from_state='play',
        to_state='CONDITION',
        func=create_condition,
    )
    action_table['JUMP2']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='CONDITION',
        func=create_condition,
    )
    action_table['JUMP2']['if'] = make_reduce_action(
        from_state='if',
        to_state='CONDITION',
        func=create_condition,
    )
    action_table['JUMP2']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='CONDITION',
        func=create_condition,
    )
    action_table['JUMP2']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='CONDITION',
        func=create_condition,
    )
    action_table['JUMP2']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='CONDITION',
        func=create_condition,
    )
    action_table['JUMP2']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='CONDITION',
        func=create_condition,
    )

    action_table['bool_op']['counter_name'] = make_shift_action(from_state='counter_name', to_state='counter_name1')
    action_table['bool_op']['flag_name'] = make_shift_action(from_state='flag_name', to_state='flag_name1')
    action_table['bool_op']['not'] = make_shift_action(from_state='not', to_state='not')

    action_table['is']['bool'] = make_shift_action(from_state='bool', to_state='bool1')

    action_table['comparator_op']['digit'] = make_shift_action(from_state='digit', to_state='digit1')

    action_table['PREDICATE2']['bool_op'] = make_shift_action(from_state='bool_op', to_state='bool_op')
    action_table['PREDICATE2']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='NOT_PRED',
        func=create_not_predicate,
    )

    action_table['TexT2']['label'] = make_reduce_action(
        from_state='label',
        to_state='PHRASE_NO_OPTIONS',
        func=create_phrase_without_options,
    )
    action_table['TexT2']['set'] = make_reduce_action(
        from_state='set',
        to_state='PHRASE_NO_OPTIONS',
        func=create_phrase_without_options,
    )
    action_table['TexT2']['play'] = make_reduce_action(
        from_state='play',
        to_state='PHRASE_NO_OPTIONS',
        func=create_phrase_without_options,
    )
    action_table['TexT2']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='PHRASE_NO_OPTIONS',
        func=create_phrase_without_options,
    )
    action_table['TexT2']['if'] = make_reduce_action(
        from_state='if',
        to_state='PHRASE_NO_OPTIONS',
        func=create_phrase_without_options,
    )
    action_table['TexT2']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='PHRASE_NO_OPTIONS',
        func=create_phrase_without_options,
    )
    action_table['TexT2']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='PHRASE_NO_OPTIONS',
        func=create_phrase_without_options,
    )
    action_table['TexT2']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='PHRASE_NO_OPTIONS',
        func=create_phrase_without_options,
    )
    action_table['TexT2']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='PHRASE_NO_OPTIONS',
        func=create_phrase_without_options,
    )

    action_table['colon3']['TexT'] = make_shift_action(from_state='TexT', to_state='TexT5')

    action_table['position']['comma'] = make_shift_action(from_state='comma', to_state='comma1')
    action_table['position']['close_bracket'] = make_shift_action(from_state='close_bracket', to_state='close_bracket1')

    action_table['emotion1']['close_bracket'] = make_shift_action(from_state='close_bracket', to_state='close_bracket2')

    action_table['colon4']['label'] = make_shift_action(from_state='label', to_state='label3')

    action_table['VARIANTLIST`']['label'] = make_reduce_action(
        from_state='label',
        to_state='VARIANTLIST',
        func=update_variant_list,
    )
    action_table['VARIANTLIST`']['set'] = make_reduce_action(
        from_state='set',
        to_state='VARIANTLIST',
        func=update_variant_list,
    )
    action_table['VARIANTLIST`']['play'] = make_reduce_action(
        from_state='play',
        to_state='VARIANTLIST',
        func=update_variant_list,
    )
    action_table['VARIANTLIST`']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='VARIANTLIST',
        func=update_variant_list,
    )
    action_table['VARIANTLIST`']['if'] = make_reduce_action(
        from_state='if',
        to_state='VARIANTLIST',
        func=update_variant_list,
    )
    action_table['VARIANTLIST`']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='VARIANTLIST',
        func=update_variant_list,
    )
    action_table['VARIANTLIST`']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='VARIANTLIST',
        func=update_variant_list,
    )
    action_table['VARIANTLIST`']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='VARIANTLIST',
        func=update_variant_list,
    )
    action_table['VARIANTLIST`']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='VARIANTLIST',
        func=update_variant_list,
    )

    action_table['VARIANT2']['label'] = make_reduce_action(
        from_state='label',
        to_state='VARIANTLIST`',
        func=create_variant_list_b,
    )
    action_table['VARIANT2']['set'] = make_reduce_action(
        from_state='set',
        to_state='VARIANTLIST`',
        func=create_variant_list_b,
    )
    action_table['VARIANT2']['play'] = make_reduce_action(
        from_state='play',
        to_state='VARIANTLIST`',
        func=create_variant_list_b,
    )
    action_table['VARIANT2']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='VARIANTLIST`',
        func=create_variant_list_b,
    )
    action_table['VARIANT2']['tab'] = make_shift_action(from_state='tab', to_state='tab')
    action_table['VARIANT2']['if'] = make_reduce_action(
        from_state='if',
        to_state='VARIANTLIST`',
        func=create_variant_list_b,
    )
    action_table['VARIANT2']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='VARIANTLIST`',
        func=create_variant_list_b,
    )
    action_table['VARIANT2']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='VARIANTLIST`',
        func=create_variant_list_b,
    )
    action_table['VARIANT2']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='VARIANTLIST`',
        func=create_variant_list_b,
    )
    action_table['VARIANT2']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='VARIANTLIST`',
        func=create_variant_list_b,
    )

    action_table['TexT3']['colon'] = make_shift_action(from_state='colon', to_state='colon6')

    action_table['TexT4']['TexT'] = make_reduce_action(
        from_state='tab', to_state='PHRASE_NO_OPTIONS', func=create_phrase_without_options
    )

    action_table['colon5']['TexT'] = make_shift_action(from_state='TexT', to_state='TexT6')

    action_table['PREDICATE3']['bool_op'] = make_shift_action(from_state='bool_op', to_state='bool_op')
    action_table['PREDICATE3']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='COMB_PRED',
        func=create_comb_predicate,
    )

    action_table['bool1']['bool_op'] = make_reduce_action(
        from_state='bool_op',
        to_state='PREDICATE',
        func=create_condition_flag,
    )
    action_table['bool1']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='PREDICATE',
        func=create_condition_flag,
    )

    action_table['digit1']['bool_op'] = make_reduce_action(
        from_state='bool_op',
        to_state='PREDICATE',
        func=create_condition_counter,
    )
    action_table['digit1']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='PREDICATE',
        func=create_condition_counter,
    )

    action_table['TexT5']['label'] = make_reduce_action(
        from_state='label',
        to_state='PHRASE',
        func=create_phrase,
    )
    action_table['TexT5']['set'] = make_reduce_action(
        from_state='set',
        to_state='PHRASE',
        func=create_phrase,
    )

    action_table['TexT5']['play'] = make_reduce_action(
        from_state='play',
        to_state='PHRASE',
        func=create_phrase,
    )
    action_table['TexT5']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='PHRASE',
        func=create_phrase,
    )
    action_table['TexT5']['if'] = make_reduce_action(
        from_state='if',
        to_state='PHRASE',
        func=create_phrase,
    )
    action_table['TexT5']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='PHRASE',
        func=create_phrase,
    )
    action_table['TexT5']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='PHRASE',
        func=create_phrase,
    )
    action_table['TexT5']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='PHRASE',
        func=create_phrase,
    )
    action_table['TexT5']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='PHRASE',
        func=create_phrase,
    )

    action_table['comma1']['emotion'] = make_shift_action(from_state='emotion', to_state='emotion2')

    action_table['close_bracket1']['colon'] = make_reduce_action(
        from_state='colon',
        to_state='OPTIONS',
        func=create_options_position,
    )

    action_table['close_bracket2']['colon'] = make_reduce_action(
        from_state='colon',
        to_state='OPTIONS',
        func=create_options_emotion,
    )

    action_table['label3']['load'] = make_reduce_action(
        from_state='eof',
        to_state='WHLOAD',
        func=create_load_character,
    )
    action_table['label3']['label'] = make_reduce_action(
        from_state='label',
        to_state='WHLOAD',
        func=create_load_character,
    )
    action_table['label3']['set'] = make_reduce_action(
        from_state='set',
        to_state='WHLOAD',
        func=create_load_character,
    )
    action_table['label3']['play'] = make_reduce_action(
        from_state='play',
        to_state='WHLOAD',
        func=create_load_character,
    )
    action_table['label3']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='WHLOAD',
        func=create_load_character,
    )
    action_table['label3']['if'] = make_reduce_action(
        from_state='if',
        to_state='WHLOAD',
        func=create_load_character,
    )
    action_table['label3']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='WHLOAD',
        func=create_load_character,
    )
    action_table['label3']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='WHLOAD',
        func=create_load_character,
    )
    action_table['label3']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='WHLOAD',
        func=create_load_character,
    )

    action_table['colon6']['label'] = make_reduce_action(
        from_state='label',
        to_state='VARIANTLIST`',
        func=update_variant_list_b,
    )
    action_table['colon6']['set'] = make_reduce_action(
        from_state='set',
        to_state='VARIANTLIST`',
        func=update_variant_list_b,
    )
    action_table['colon6']['play'] = make_reduce_action(
        from_state='play',
        to_state='VARIANTLIST`',
        func=update_variant_list_b,
    )
    action_table['colon6']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='VARIANTLIST`',
        func=update_variant_list_b,
    )
    action_table['colon6']['if'] = make_reduce_action(
        from_state='if',
        to_state='VARIANTLIST`',
        func=update_variant_list_b,
    )
    action_table['colon6']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='VARIANTLIST`',
        func=update_variant_list_b,
    )
    action_table['colon6']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='VARIANTLIST`',
        func=update_variant_list_b,
    )
    action_table['colon6']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='VARIANTLIST`',
        func=update_variant_list_b,
    )
    action_table['colon6']['flag_name'] = make_shift_action(
        from_state='flag_name',
        to_state='flag_name2`',
    )
    action_table['colon6']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='VARIANTLIST`',
        func=update_variant_list_b,
    )

    action_table['VARIANT3']['counter_name'] = make_shift_action(from_state='counter_name', to_state='counter_name2')
    action_table['VARIANT3']['flag_name'] = make_shift_action(from_state='flag_name', to_state='flag_name2')

    action_table['TexT6']['tab'] = make_reduce_action(
        from_state='tab',
        to_state='PHRASE',
        func=create_phrase,
    )

    action_table['emotion2']['close_bracket'] = make_shift_action(from_state='close_bracket', to_state='close_bracket3')

    action_table['EFFECTLIST']['label'] = make_reduce_action(
        from_state='label',
        to_state='VARIANT',
        func=create_variant,
    )
    action_table['EFFECTLIST']['set'] = make_reduce_action(
        from_state='set',
        to_state='VARIANT',
        func=create_variant,
    )
    action_table['EFFECTLIST']['play'] = make_reduce_action(
        from_state='play',
        to_state='VARIANT',
        func=create_variant,
    )
    action_table['EFFECTLIST']['comma'] = make_shift_action(from_state='comma', to_state='comma2')
    action_table['EFFECTLIST']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='VARIANT',
        func=create_variant,
    )
    action_table['EFFECTLIST']['tab'] = make_reduce_action(
        from_state='tab',
        to_state='VARIANT',
        func=create_variant,
    )
    action_table['EFFECTLIST']['if'] = make_reduce_action(
        from_state='if',
        to_state='VARIANT',
        func=create_variant,
    )
    action_table['EFFECTLIST']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='VARIANT',
        func=create_variant,
    )
    action_table['EFFECTLIST']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='VARIANT',
        func=create_variant,
    )
    action_table['EFFECTLIST']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='VARIANT',
        func=create_variant,
    )
    action_table['EFFECTLIST']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='VARIANT',
        func=create_variant,
    )

    action_table['EFFECT1']['label'] = make_reduce_action(
        from_state='label',
        to_state='EFFECTLIST',
        func=create_effect_list,
    )
    action_table['EFFECT1']['set'] = make_reduce_action(
        from_state='set',
        to_state='EFFECTLIST',
        func=create_effect_list,
    )
    action_table['EFFECT1']['play'] = make_reduce_action(
        from_state='play',
        to_state='EFFECTLIST',
        func=create_effect_list,
    )
    action_table['EFFECT1']['comma'] = make_reduce_action(
        from_state='play',
        to_state='EFFECTLIST',
        func=create_effect_list,
    )
    action_table['EFFECT1']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='EFFECTLIST',
        func=create_effect_list,
    )
    action_table['EFFECT1']['tab'] = make_reduce_action(
        from_state='tab',
        to_state='EFFECTLIST',
        func=create_effect_list,
    )
    action_table['EFFECT1']['if'] = make_reduce_action(
        from_state='if',
        to_state='EFFECTLIST',
        func=create_effect_list,
    )
    action_table['EFFECT1']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='EFFECTLIST',
        func=create_effect_list,
    )
    action_table['EFFECT1']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='EFFECTLIST',
        func=create_effect_list,
    )
    action_table['EFFECT1']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='EFFECTLIST',
        func=create_effect_list,
    )
    action_table['EFFECT1']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='EFFECTLIST',
        func=create_effect_list,
    )

    action_table['counter_name2']['digit_op'] = make_shift_action(from_state='digit_op', to_state='digit_op1')

    action_table['flag_name2']['equals'] = make_shift_action(from_state='equals', to_state='equals1')

    action_table['close_bracket3']['colon'] = make_reduce_action(
        from_state='colon',
        to_state='OPTIONS',
        func=create_options_position_and_emotion,
    )

    action_table['EFFECT2']['label'] = make_reduce_action(
        from_state='label',
        to_state='EFFECTLIST',
        func=update_effect_list,
    )
    action_table['EFFECT2']['set'] = make_reduce_action(
        from_state='set',
        to_state='EFFECTLIST',
        func=update_effect_list,
    )
    action_table['EFFECT2']['play'] = make_reduce_action(
        from_state='play',
        to_state='EFFECTLIST',
        func=update_effect_list,
    )
    action_table['EFFECT2']['comma'] = make_reduce_action(
        from_state='comma',
        to_state='EFFECTLIST',
        func=update_effect_list,
    )
    action_table['EFFECT2']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='EFFECTLIST',
        func=update_effect_list,
    )
    action_table['EFFECT2']['tab'] = make_reduce_action(
        from_state='tab',
        to_state='EFFECTLIST',
        func=update_effect_list,
    )
    action_table['EFFECT2']['if'] = make_reduce_action(
        from_state='if',
        to_state='EFFECTLIST',
        func=update_effect_list,
    )
    action_table['EFFECT2']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='EFFECTLIST',
        func=update_effect_list,
    )
    action_table['EFFECT2']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='EFFECTLIST',
        func=update_effect_list,
    )
    action_table['EFFECT2']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='EFFECTLIST',
        func=update_effect_list,
    )
    action_table['EFFECT2']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='EFFECTLIST',
        func=update_effect_list,
    )

    action_table['digit2']['label'] = make_reduce_action(
        from_state='label',
        to_state='EFFECT',
        func=create_effect_counter,
    )
    action_table['digit2']['set'] = make_reduce_action(
        from_state='set',
        to_state='EFFECT',
        func=create_effect_counter,
    )
    action_table['digit2']['play'] = make_reduce_action(
        from_state='play',
        to_state='EFFECT',
        func=create_effect_counter,
    )
    action_table['digit2']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='EFFECT',
        func=create_effect_counter,
    )
    action_table['digit2']['tab'] = make_reduce_action(
        from_state='tab',
        to_state='EFFECT',
        func=create_effect_counter,
    )
    action_table['digit2']['if'] = make_reduce_action(
        from_state='if',
        to_state='EFFECT',
        func=create_effect_counter,
    )
    action_table['digit2']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='EFFECT',
        func=create_effect_counter,
    )
    action_table['digit2']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='EFFECT',
        func=create_effect_counter,
    )
    action_table['digit2']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='EFFECT',
        func=create_effect_counter,
    )
    action_table['digit2']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='EFFECT',
        func=create_effect_counter,
    )

    action_table['bool2']['label'] = make_reduce_action(
        from_state='label',
        to_state='EFFECT',
        func=create_effect_flag,
    )
    action_table['bool2']['set'] = make_reduce_action(
        from_state='set',
        to_state='EFFECT',
        func=create_effect_flag,
    )
    action_table['bool2']['play'] = make_reduce_action(
        from_state='play',
        to_state='EFFECT',
        func=create_effect_flag,
    )
    action_table['bool2']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='EFFECT',
        func=create_effect_flag,
    )
    action_table['bool2']['tab'] = make_reduce_action(
        from_state='tab',
        to_state='EFFECT',
        func=create_effect_flag,
    )
    action_table['bool2']['if'] = make_reduce_action(
        from_state='if',
        to_state='EFFECT',
        func=create_effect_flag,
    )
    action_table['bool2']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='EFFECT',
        func=create_effect_flag,
    )
    action_table['bool2']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='EFFECT',
        func=create_effect_flag,
    )
    action_table['bool2']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='EFFECT',
        func=create_effect_flag,
    )
    action_table['bool2']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='EFFECT',
        func=create_effect_flag,
    )

    action_table['digit3']['label'] = make_reduce_action(
        from_state='label',
        to_state='EFFECT',
        func=create_effect_counter,
    )
    action_table['digit3']['set'] = make_reduce_action(
        from_state='set',
        to_state='EFFECT',
        func=create_effect_counter,
    )
    action_table['digit3']['play'] = make_reduce_action(
        from_state='play',
        to_state='EFFECT',
        func=create_effect_counter,
    )
    action_table['digit3']['comma'] = make_reduce_action(
        from_state='comma',
        to_state='EFFECT',
        func=create_effect_counter,
    )
    action_table['digit3']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='EFFECT',
        func=create_effect_counter,
    )
    action_table['digit3']['tab'] = make_reduce_action(
        from_state='tab',
        to_state='EFFECT',
        func=create_effect_counter,
    )
    action_table['digit3']['if'] = make_reduce_action(
        from_state='if',
        to_state='EFFECT',
        func=create_effect_counter,
    )
    action_table['digit3']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='EFFECT',
        func=create_effect_counter,
    )
    action_table['digit3']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='EFFECT',
        func=create_effect_counter,
    )
    action_table['digit3']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='EFFECT',
        func=create_effect_counter,
    )
    action_table['digit3']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='EFFECT',
        func=create_effect_counter,
    )

    action_table['bool3']['label'] = make_reduce_action(
        from_state='label',
        to_state='EFFECT',
        func=create_effect_flag,
    )
    action_table['bool3']['set'] = make_reduce_action(
        from_state='set',
        to_state='EFFECT',
        func=create_effect_flag,
    )
    action_table['bool3']['play'] = make_reduce_action(
        from_state='play',
        to_state='EFFECT',
        func=create_effect_flag,
    )
    action_table['bool3']['comma'] = make_reduce_action(
        from_state='comma',
        to_state='EFFECT',
        func=create_effect_flag,
    )
    action_table['bool3']['choice'] = make_reduce_action(
        from_state='choice',
        to_state='EFFECT',
        func=create_effect_flag,
    )
    action_table['bool3']['tab'] = make_reduce_action(
        from_state='tab',
        to_state='EFFECT',
        func=create_effect_flag,
    )
    action_table['bool3']['if'] = make_reduce_action(
        from_state='if',
        to_state='EFFECT',
        func=create_effect_flag,
    )
    action_table['bool3']['jump'] = make_reduce_action(
        from_state='jump',
        to_state='EFFECT',
        func=create_effect_flag,
    )
    action_table['bool3']['mark'] = make_reduce_action(
        from_state='mark',
        to_state='EFFECT',
        func=create_effect_flag,
    )
    action_table['bool3']['load_scene'] = make_reduce_action(
        from_state='load_scene',
        to_state='EFFECT',
        func=create_effect_flag,
    )
    action_table['bool3']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='EFFECT',
        func=create_effect_flag,
    )

    action_table['comma2']['counter_name'] = make_shift_action(from_state='counter_name', to_state='counter_name3')
    action_table['comma2']['flag_name'] = make_shift_action(from_state='flag_name', to_state='flag_name3')

    action_table['digit_op1']['digit'] = make_shift_action(from_state='digit', to_state='digit2')

    action_table['equals1']['bool'] = make_shift_action(from_state='bool', to_state='bool2')

    action_table['counter_name3']['digit_op'] = make_shift_action(from_state='digit_op', to_state='digit_op2')

    action_table['flag_name3']['equals'] = make_shift_action(from_state='equals', to_state='equals2')

    action_table['digit_op2']['digit'] = make_shift_action(from_state='digit', to_state='digit3')

    action_table['equals2']['bool'] = make_shift_action(from_state='bool', to_state='bool3')

    return action_table


def make_goto_table():
    goto_table = dict()
    for row in ROWS:
        goto_table[row] = dict({k: None for k in COLS_GOTO})

    goto_table['DOWN']['MAIN'] = GotoCellDescriptor(new_state='MAIN', name_state='MAIN')
    goto_table['DOWN']['LOADLIST'] = GotoCellDescriptor(new_state='LOADLIST', name_state='LOADLIST')
    goto_table['DOWN']['LOAD'] = GotoCellDescriptor(new_state='LOAD', name_state='LOAD1')

    goto_table['LOADLIST']['ACTIONLIST'] = GotoCellDescriptor(new_state='ACTIONLIST', name_state='ACTIONLIST')
    goto_table['LOADLIST']['ACTION'] = GotoCellDescriptor(new_state='ACTION', name_state='ACTION1')
    goto_table['LOADLIST']['SET'] = GotoCellDescriptor(new_state='SET', name_state='SET')
    goto_table['LOADLIST']['PLAY'] = GotoCellDescriptor(new_state='PLAY', name_state='PLAY')
    goto_table['LOADLIST']['COMMON_PHRASE'] = GotoCellDescriptor(new_state='COMMON_PHRASE', name_state='COMMON_PHRASE1')
    goto_table['LOADLIST']['PHRASE_NO_OPTIONS'] = GotoCellDescriptor(
        new_state='PHRASE_NO_OPTIONS', name_state='PHRASE_NO_OPTIONS1'
    )
    goto_table['LOADLIST']['PHRASE'] = GotoCellDescriptor(new_state='PHRASE', name_state='PHRASE1')
    goto_table['LOADLIST']['CHOICE'] = GotoCellDescriptor(new_state='CHOICE', name_state='CHOICE')
    goto_table['LOADLIST']['CONDITION'] = GotoCellDescriptor(new_state='CONDITION', name_state='CONDITION')
    goto_table['LOADLIST']['JUMP'] = GotoCellDescriptor(new_state='JUMP', name_state='JUMP1')
    goto_table['LOADLIST']['MARK'] = GotoCellDescriptor(new_state='MARK', name_state='MARK')
    goto_table['LOADLIST']['LOADSCENE'] = GotoCellDescriptor(new_state='LOADSCENE', name_state='LOADSCENE')

    goto_table['ACTION1']['ACTIONLIST`'] = GotoCellDescriptor(new_state='ACTIONLIST`', name_state='ACTIONLIST`1')
    goto_table['ACTION1']['ACTION'] = GotoCellDescriptor(new_state='ACTION', name_state='ACTION2')
    goto_table['ACTION1']['SET'] = GotoCellDescriptor(new_state='SET', name_state='SET')
    goto_table['ACTION1']['PLAY'] = GotoCellDescriptor(new_state='PLAY', name_state='PLAY')
    goto_table['ACTION1']['COMMON_PHRASE'] = GotoCellDescriptor(new_state='COMMON_PHRASE', name_state='COMMON_PHRASE1')
    goto_table['ACTION1']['PHRASE_NO_OPTIONS'] = GotoCellDescriptor(
        new_state='PHRASE_NO_OPTIONS', name_state='PHRASE_NO_OPTIONS1'
    )
    goto_table['ACTION1']['PHRASE'] = GotoCellDescriptor(new_state='PHRASE', name_state='PHRASE1')
    goto_table['ACTION1']['CHOICE'] = GotoCellDescriptor(new_state='CHOICE', name_state='CHOICE')
    goto_table['ACTION1']['CONDITION'] = GotoCellDescriptor(new_state='CONDITION', name_state='CONDITION')
    goto_table['ACTION1']['JUMP'] = GotoCellDescriptor(new_state='JUMP', name_state='JUMP1')
    goto_table['ACTION1']['MARK'] = GotoCellDescriptor(new_state='MARK', name_state='MARK')
    goto_table['ACTION1']['LOADSCENE'] = GotoCellDescriptor(new_state='LOADSCENE', name_state='LOADSCENE')

    goto_table['ACTION2']['ACTIONLIST`'] = GotoCellDescriptor(new_state='ACTIONLIST`', name_state='ACTIONLIST`2')
    goto_table['ACTION2']['ACTION'] = GotoCellDescriptor(new_state='ACTION', name_state='ACTION2')
    goto_table['ACTION2']['SET'] = GotoCellDescriptor(new_state='SET', name_state='SET')
    goto_table['ACTION2']['PLAY'] = GotoCellDescriptor(new_state='PLAY', name_state='PLAY')
    goto_table['ACTION2']['COMMON_PHRASE'] = GotoCellDescriptor(new_state='COMMON_PHRASE', name_state='COMMON_PHRASE1')
    goto_table['ACTION2']['PHRASE_NO_OPTIONS'] = GotoCellDescriptor(
        new_state='PHRASE_NO_OPTIONS', name_state='PHRASE_NO_OPTIONS1'
    )
    goto_table['ACTION2']['PHRASE'] = GotoCellDescriptor(new_state='PHRASE', name_state='PHRASE1')
    goto_table['ACTION2']['CHOICE'] = GotoCellDescriptor(new_state='CHOICE', name_state='CHOICE')
    goto_table['ACTION2']['CONDITION'] = GotoCellDescriptor(new_state='CONDITION', name_state='CONDITION')
    goto_table['ACTION2']['JUMP'] = GotoCellDescriptor(new_state='JUMP', name_state='JUMP1')
    goto_table['ACTION2']['MARK'] = GotoCellDescriptor(new_state='MARK', name_state='MARK')
    goto_table['ACTION2']['LOADSCENE'] = GotoCellDescriptor(new_state='LOADSCENE', name_state='LOADSCENE')

    goto_table['LOAD1']['LOADLIST`'] = GotoCellDescriptor(new_state='LOADLIST`', name_state='LOADLIST`1')
    goto_table['LOAD1']['LOAD'] = GotoCellDescriptor(new_state='LOAD', name_state='LOAD2')

    goto_table['load']['WHLOAD'] = GotoCellDescriptor(new_state='WHLOAD', name_state='WHLOAD')

    goto_table['set']['WHSET'] = GotoCellDescriptor(new_state='WHSET', name_state='WHSET')

    goto_table['play']['WHPLAY'] = GotoCellDescriptor(new_state='WHPLAY', name_state='WHPLAY')

    goto_table['choice']['COMMON_PHRASE'] = GotoCellDescriptor(new_state='COMMON_PHRASE', name_state='COMMON_PHRASE2')
    goto_table['choice']['PHRASE_NO_OPTIONS'] = GotoCellDescriptor(
        new_state='PHRASE_NO_OPTIONS', name_state='PHRASE_NO_OPTIONS2'
    )
    goto_table['choice']['PHRASE'] = GotoCellDescriptor(new_state='PHRASE', name_state='PHRASE2')

    goto_table['if']['PREDICATE'] = GotoCellDescriptor(new_state='PREDICATE', name_state='PREDICATE1')
    goto_table['if']['COMB_PRED'] = GotoCellDescriptor(new_state='COMB_PRED', name_state='COMB_PRED')
    goto_table['if']['NOT_PRED'] = GotoCellDescriptor(new_state='NOT_PRED', name_state='NOT_PRED')

    goto_table['label1']['OPTIONS'] = GotoCellDescriptor(new_state='OPTIONS', name_state='OPTIONS1')

    goto_table['LOAD2']['LOADLIST`'] = GotoCellDescriptor(new_state='LOADLIST`', name_state='LOADLIST`2')
    goto_table['LOAD2']['LOAD'] = GotoCellDescriptor(new_state='LOAD', name_state='LOAD2')

    goto_table['COMMON_PHRASE2']['VARIANTLIST'] = GotoCellDescriptor(new_state='VARIANTLIST', name_state='VARIANTLIST')
    goto_table['COMMON_PHRASE2']['VARIANT'] = GotoCellDescriptor(new_state='VARIANT', name_state='VARIANT1')

    goto_table['label2']['OPTIONS'] = GotoCellDescriptor(new_state='OPTIONS', name_state='OPTIONS2')

    goto_table['PREDICATE1']['JUMP'] = GotoCellDescriptor(new_state='JUMP', name_state='JUMP2')

    goto_table['not']['PREDICATE'] = GotoCellDescriptor(new_state='PREDICATE', name_state='PREDICATE2')
    goto_table['not']['COMB_PRED'] = GotoCellDescriptor(new_state='COMB_PRED', name_state='COMB_PRED')
    goto_table['not']['NOT_PRED'] = GotoCellDescriptor(new_state='NOT_PRED', name_state='NOT_PRED')

    goto_table['VARIANT1']['VARIANTLIST`'] = GotoCellDescriptor(new_state='VARIANTLIST`', name_state='VARIANTLIST`')
    goto_table['VARIANT1']['VARIANT'] = GotoCellDescriptor(new_state='VARIANT', name_state='VARIANT2')

    goto_table['bool_op']['PREDICATE'] = GotoCellDescriptor(new_state='PREDICATE', name_state='PREDICATE3')
    goto_table['bool_op']['COMB_PRED'] = GotoCellDescriptor(new_state='COMB_PRED', name_state='COMB_PRED')
    goto_table['bool_op']['NOT_PRED'] = GotoCellDescriptor(new_state='NOT_PRED', name_state='NOT_PRED')

    goto_table['VARIANT2']['VARIANTLIST`'] = GotoCellDescriptor(new_state='VARIANTLIST`', name_state='VARIANTLIST`')
    goto_table['VARIANT2']['VARIANT'] = GotoCellDescriptor(new_state='VARIANT', name_state='VARIANT2')

    goto_table['VARIANT3']['EFFECTLIST'] = GotoCellDescriptor(new_state='EFFECTLIST', name_state='EFFECTLIST')
    goto_table['VARIANT3']['EFFECT'] = GotoCellDescriptor(new_state='EFFECT', name_state='EFFECT1')

    goto_table['comma2']['EFFECT'] = GotoCellDescriptor(new_state='EFFECT', name_state='EFFECT2')

    return goto_table


_tokens = [
    TokenDesctiptor(name='None', pattern='[ \n\r]+'),
    TokenDesctiptor(name='comment', pattern='#[\\w\\d ]*#'),
    TokenDesctiptor(name='load_scene', pattern='load_scene'),
    TokenDesctiptor(name='load', pattern='load'),
    TokenDesctiptor(name='tab', pattern='\\t'),
    TokenDesctiptor(name='choice', pattern='choice'),
    TokenDesctiptor(name='character', pattern='character'),
    TokenDesctiptor(name='image', pattern='image'),
    TokenDesctiptor(name='sound', pattern='sound'),
    TokenDesctiptor(name='play', pattern='play'),
    TokenDesctiptor(name='set', pattern='set'),
    TokenDesctiptor(name='jump', pattern='jump'),
    TokenDesctiptor(name='background', pattern='background'),
    TokenDesctiptor(name='text', pattern='text'),
    TokenDesctiptor(name='blackout', pattern='blackout'),
    TokenDesctiptor(name='position', pattern='(left|center|right)'),
    TokenDesctiptor(name='mark', pattern='mark[^_]'),
    TokenDesctiptor(name='if', pattern='if'),
    TokenDesctiptor(name='bool_op', pattern='(and|or)'),
    TokenDesctiptor(name='not', pattern='not'),
    TokenDesctiptor(name='is', pattern='is'),
    TokenDesctiptor(name='colon', pattern=':'),
    TokenDesctiptor(name='open_bracket', pattern='\\('),
    TokenDesctiptor(name='close_bracket', pattern='\\)'),
    TokenDesctiptor(name='comma', pattern=','),
    TokenDesctiptor(name='equals', pattern='='),
    TokenDesctiptor(name='digit', pattern='([0-9]|[1-9][0-9]+)'),
    TokenDesctiptor(name='digit_op', pattern='(-|\\+)'),
    TokenDesctiptor(name='bool', pattern='(true|false)'),
    TokenDesctiptor(name='comparator_op', pattern='[<|>]=?'),
    TokenDesctiptor(name='mark_name', pattern='mark_[_\\w]+'),
    TokenDesctiptor(name='counter_name', pattern='counter_[_\\w]+'),
    TokenDesctiptor(name='flag_name', pattern='flag_[_\\w]+'),
    TokenDesctiptor(name='path', pattern="\\'\\w[\\w\\d./\\\\]+\\'"),
    TokenDesctiptor(name='emotion', pattern='\\w_[\\w]+'),
    TokenDesctiptor(name='TexT', pattern='\"[ \\.\\,\\-\\!\\?\\w\\d\\{\\}<>/`]*\"'),
    TokenDesctiptor(name='word', pattern='\\w[_\\w]+'),
    TokenDesctiptor(name='label', pattern='\\w'),
]

scene = Config(_tokens, make_action_table(), make_goto_table())
