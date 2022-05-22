from config.reader import parse_actions, parse_goto, parse_tokens, reader_config
from lrparser.utils.action_table_descriptor import ReduceFunc

update_character_list: ReduceFunc = lambda CS, C: {
    "list": [*CS.get("list"), C.get("char")]
}
create_character_list: ReduceFunc = lambda CC: {"list": [CC.get("char")]}

update_sprite_list: ReduceFunc = lambda SS, S: {
    "list": [*SS.get("list"), S.get("sprite")]
}
create_sprite_list: ReduceFunc = lambda S: {"list": [S.get("sprite")]}

create_character_without_sprites: ReduceFunc = lambda c, n: {
    "char": {"name": n.get("val")}
}
create_character: ReduceFunc = lambda c, n, col, SS: {
    "char": {"name": n.get("val"), "sprites": SS.get("list")}
}

wrap_character_without_sprites: ReduceFunc = lambda CNS: {
    "char": CNS.get("char")
}

wrap_character: ReduceFunc = lambda C: {"char": C.get("char")}

create_sprite: ReduceFunc = lambda t, f, e, p: {
    "sprite": {"field": f.get("val"), "path": p.get("val")[1:-1]}
}

prepare_result: ReduceFunc = lambda CS, e: {"res": CS.get("list")}


funcs: dict[str, ReduceFunc] = {
    "updateCharacterList": update_character_list,
    "createCharacterList": create_character_list,
    "updateSpriteList": update_sprite_list,
    "createSpriteList": create_sprite_list,
    "createCharacterWithoutSprites": create_character_without_sprites,
    "createCharacter": create_character,
    "wrapCharacterWithoutSprite": wrap_character_without_sprites,
    "wrapCharacter": wrap_character,
    "createSprite": create_sprite,
    "prepareResult": prepare_result,
}

json_config = reader_config("config/character_config.json")

tokens = parse_tokens(json_config)
actions = parse_actions(json_config, funcs)
goto = parse_goto(json_config)
