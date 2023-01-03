from typing import Any

from config.common import (
    ActionCellDescriptor,
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
    'CHARACTER_LIST',
    'COMMON_CHARACTER1',
    'CHARACTER',
    'CHARACTER_NO_SPRITE',
    'character',
    'CHARACTER_LIST`1',
    'COMMON_CHARACTER2',
    'name1',
    'CHARACTER_LIST`2',
    'colon',
    'SPRITE_BLOCK',
    'tab1',
    'SPRITE_LIST',
    'SPRITE1',
    'name2',
    'SPRITE_LIST`1',
    'tab2',
    'equals',
    'SPRITE2',
    'path',
    'SPRITE_LIST`2',
)
COLS_ACTION = ('character', 'name1', 'colon', 'tab', 'name2', 'equals', 'path', 'eof')
COLS_GOTO = (
    "S'",
    'MAIN',
    'CHARACTER_LIST',
    'CHARACTER_LIST`',
    'COMMON_CHARACTER',
    'CHARACTER',
    'CHARACTER_NO_SPRITE',
    'SPRITE_BLOCK',
    'SPRITE_LIST',
    'SPRITE_LIST`',
    'SPRITE',
)


def prepare_result(CL) -> dict[str, Any]:
    return {'res': CL.get('list')}


def create_character_list(CC) -> dict[str, Any]:
    return {'list': [CC.get('char')]}


def update_character_list(CC, CL) -> dict[str, Any]:
    return {'list': [*CL.get('list'), CC.get('char')]}


def create_character_list_b(CC) -> dict[str, Any]:
    return {'list': [CC.get('char')]}


def update_character_list_b(CC, CL) -> dict[str, Any]:
    return {'list': [*CL.get('list'), CC.get('char')]}


def wrap_character(C) -> dict[str, Any]:
    return {'char': C.get('char')}


def wrap_character_without_sprites(CNS) -> dict[str, Any]:
    return {'char': CNS.get('char')}


def create_character(c, n, col, SB) -> dict[str, Any]:
    return {'char': {'name': n.get('val'), 'sprites': SB.get('list')}}


def create_character_without_sprites(c, n) -> dict[str, Any]:
    return {'char': {'name': n.get('val')}}


def create_sprite_block(t, SL) -> dict[str, Any]:
    return {'list': SL.get('list')}


def create_sprite_list(S) -> dict[str, Any]:
    return {'list': [S.get('sprite')]}


def update_sprite_list(S, SS) -> dict[str, Any]:
    return {'list': [*SS.get('list'), S.get('sprite')]}


def create_sprite_list_b(t, S) -> dict[str, Any]:
    return {'list': [S.get('sprite')]}


def update_sprite_list_b(t, S, SS) -> dict[str, Any]:
    return {'list': [*SS.get('list'), S.get('sprite')]}


def create_sprite(f, e, p) -> dict[str, Any]:
    return {'sprite': {'field': f.get('val'), 'path': p.get('val')[1:-1]}}


def make_action_table():
    action_table = dict()
    for row in ROWS:
        action_table[row] = dict({k: None for k in COLS_ACTION})

    action_table['DOWN']['character'] = make_shift_action(from_state='character', to_state='character')
    action_table['MAIN']['eof'] = make_finish_action(from_state='eof')
    action_table['CHARACTER_LIST']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='MAIN',
        func=prepare_result,
    )
    action_table['COMMON_CHARACTER1']['character'] = make_shift_action(from_state='character', to_state='character')
    action_table['COMMON_CHARACTER1']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='CHARACTER_LIST',
        func=create_character_list,
    )
    action_table['CHARACTER']['character'] = make_reduce_action(
        from_state='character',
        to_state='COMMON_CHARACTER',
        func=wrap_character,
    )
    action_table['CHARACTER']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='COMMON_CHARACTER',
        func=wrap_character,
    )
    action_table['CHARACTER_NO_SPRITE']['character'] = make_reduce_action(
        from_state='character',
        to_state='COMMON_CHARACTER',
        func=wrap_character_without_sprites,
    )
    action_table['CHARACTER_NO_SPRITE']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='COMMON_CHARACTER',
        func=wrap_character_without_sprites,
    )
    action_table['character']['name'] = make_shift_action(from_state='name', to_state='name1')
    action_table['CHARACTER_LIST`1']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='CHARACTER_LIST',
        func=update_character_list,
    )
    action_table['COMMON_CHARACTER2']['character'] = make_shift_action(from_state='character', to_state='character')
    action_table['COMMON_CHARACTER2']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='CHARACTER_LIST`',
        func=create_character_list_b,
    )
    action_table['name1']['character'] = make_reduce_action(
        from_state='character',
        to_state='CHARACTER_NO_SPRITE',
        func=create_character_without_sprites,
    )
    action_table['name1']['colon'] = make_shift_action(from_state='colon', to_state='colon')
    action_table['name1']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='CHARACTER_NO_SPRITE',
        func=create_character_without_sprites,
    )
    action_table['CHARACTER_LIST`2']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='CHARACTER_LIST`',
        func=update_character_list_b,
    )
    action_table['colon']['tab'] = make_shift_action(from_state='tab', to_state='tab1')
    action_table['SPRITE_BLOCK']['character'] = make_reduce_action(
        from_state='character',
        to_state='CHARACTER',
        func=create_character,
    )
    action_table['SPRITE_BLOCK']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='CHARACTER',
        func=create_character,
    )
    action_table['tab1']['name'] = make_shift_action(from_state='name', to_state='name2')
    action_table['SPRITE_LIST']['character'] = make_reduce_action(
        from_state='character',
        to_state='SPRITE_BLOCK',
        func=create_sprite_block,
    )
    action_table['SPRITE_LIST']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='SPRITE_BLOCK',
        func=create_sprite_block,
    )
    action_table['SPRITE1']['character'] = make_reduce_action(
        from_state='character',
        to_state='SPRITE_LIST',
        func=create_sprite_list,
    )
    action_table['SPRITE1']['tab'] = make_shift_action(from_state='tab', to_state='tab2')
    action_table['SPRITE1']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='SPRITE_LIST',
        func=create_sprite_list,
    )
    action_table['name2']['equals'] = make_shift_action(from_state='equals', to_state='equals')
    action_table['SPRITE_LIST`1']['character'] = make_reduce_action(
        from_state='character',
        to_state='SPRITE_LIST',
        func=update_sprite_list,
    )
    action_table['SPRITE_LIST`1']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='SPRITE_LIST',
        func=update_sprite_list,
    )
    action_table['tab2']['name'] = make_shift_action(from_state='name', to_state='name2')
    action_table['equals']['path'] = make_shift_action(from_state='path', to_state='path')
    action_table['SPRITE2']['character'] = make_reduce_action(
        from_state='character',
        to_state='SPRITE_LIST`',
        func=create_sprite_list_b,
    )
    action_table['SPRITE2']['tab'] = make_shift_action(from_state='tab', to_state='tab2')
    action_table['SPRITE2']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='SPRITE_LIST`',
        func=create_sprite_list_b,
    )
    action_table['path']['character'] = make_reduce_action(
        from_state='character',
        to_state='SPRITE',
        func=create_sprite,
    )
    action_table['path']['tab'] = make_reduce_action(
        from_state='tab',
        to_state='SPRITE',
        func=create_sprite,
    )
    action_table['path']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='SPRITE',
        func=create_sprite,
    )
    action_table['SPRITE_LIST`2']['character'] = make_reduce_action(
        from_state='character',
        to_state='SPRITE_LIST`',
        func=update_sprite_list_b,
    )
    action_table['SPRITE_LIST`2']['eof'] = make_reduce_action(
        from_state='eof',
        to_state='SPRITE_LIST`',
        func=update_sprite_list_b,
    )

    return action_table


def make_goto_table():
    goto_table = dict()
    for row in ROWS:
        goto_table[row] = dict({k: None for k in COLS_GOTO})

    goto_table['DOWN']['MAIN'] = GotoCellDescriptor(new_state='MAIN', name_state='MAIN')
    goto_table['DOWN']['CHARACTER_LIST'] = GotoCellDescriptor(new_state='CHARACTER_LIST', name_state='CHARACTER_LIST')
    goto_table['DOWN']['COMMON_CHARACTER'] = GotoCellDescriptor(
        new_state='COMMON_CHARACTER', name_state='COMMON_CHARACTER1'
    )
    goto_table['DOWN']['CHARACTER'] = GotoCellDescriptor(new_state='CHARACTER', name_state='CHARACTER')
    goto_table['DOWN']['CHARACTER_NO_SPRITE'] = GotoCellDescriptor(
        new_state='CHARACTER_NO_SPRITE', name_state='CHARACTER_NO_SPRITE'
    )
    goto_table['COMMON_CHARACTER1']['CHARACTER_LIST`'] = GotoCellDescriptor(
        new_state='CHARACTER_LIST`', name_state='CHARACTER_LIST`1'
    )
    goto_table['COMMON_CHARACTER1']['COMMON_CHARACTER'] = GotoCellDescriptor(
        new_state='COMMON_CHARACTER', name_state='COMMON_CHARACTER2'
    )
    goto_table['COMMON_CHARACTER1']['CHARACTER'] = GotoCellDescriptor(new_state='CHARACTER', name_state='CHARACTER')
    goto_table['COMMON_CHARACTER1']['CHARACTER_NO_SPRITE'] = GotoCellDescriptor(
        new_state='CHARACTER_NO_SPRITE', name_state='CHARACTER_NO_SPRITE'
    )
    goto_table['COMMON_CHARACTER2']['CHARACTER_LIST`'] = GotoCellDescriptor(
        new_state='CHARACTER_LIST`', name_state='CHARACTER_LIST`2'
    )
    goto_table['COMMON_CHARACTER2']['COMMON_CHARACTER'] = GotoCellDescriptor(
        new_state='COMMON_CHARACTER', name_state='COMMON_CHARACTER2'
    )
    goto_table['COMMON_CHARACTER2']['CHARACTER'] = GotoCellDescriptor(new_state='CHARACTER', name_state='CHARACTER')
    goto_table['COMMON_CHARACTER2']['CHARACTER_NO_SPRITE'] = GotoCellDescriptor(
        new_state='CHARACTER_NO_SPRITE', name_state='CHARACTER_NO_SPRITE'
    )
    goto_table['colon']['SPRITE_BLOCK'] = GotoCellDescriptor(new_state='SPRITE_BLOCK', name_state='SPRITE_BLOCK')
    goto_table['tab1']['SPRITE_LIST'] = GotoCellDescriptor(new_state='SPRITE_LIST', name_state='SPRITE_LIST')
    goto_table['tab1']['SPRITE'] = GotoCellDescriptor(new_state='SPRITE', name_state='SPRITE1')
    goto_table['SPRITE1']['SPRITE_LIST`'] = GotoCellDescriptor(new_state='SPRITE_LIST`', name_state='SPRITE_LIST`1')
    goto_table['tab2']['SPRITE'] = GotoCellDescriptor(new_state='SPRITE', name_state='SPRITE2')
    goto_table['SPRITE2']['SPRITE_LIST`'] = GotoCellDescriptor(new_state='SPRITE_LIST`', name_state='SPRITE_LIST`2')

    return goto_table


_tokens = [
    TokenDesctiptor(name='tab', pattern='\t'),
    TokenDesctiptor(name='None', pattern='[ \n\r]+'),
    TokenDesctiptor(name='colon', pattern=':'),
    TokenDesctiptor(name='equals', pattern='='),
    TokenDesctiptor(name='character', pattern='Character'),
    TokenDesctiptor(name='name', pattern='playerName'),
    TokenDesctiptor(name='path', pattern='\"[\\w\\d./\\ ]*\"'),
    TokenDesctiptor(name='comment', pattern='#[\\w\\d ]*#'),
    TokenDesctiptor(name='name', pattern='[\\w]+'),
]

character = Config(_tokens, make_action_table(), make_goto_table())
