from config.reader import parse_actions, parse_goto, parse_tokens, reader_config
from lrparser.utils.action_table_descriptor import ReduceFunc

update_character_list: ReduceFunc = lambda CS, C: {
    "list": [*CS.get("list"), C.get("char")]
}
create_character_list: ReduceFunc = lambda C1, C2: {
    "list": [C1.get("char"), C2.get("char")]
}

update_sprite_list: ReduceFunc = lambda SS, S: {
    "list": [*SS.get("list"), S.get("sprite")]
}
create_sprite_list: ReduceFunc = lambda S1, S2: {
    "list": [S1.get("sprite"), S2.get("sprite")]
}

create_character_without_sprites: ReduceFunc = lambda c, n: {
    "char": {"name": n.get("val")}
}
create_character: ReduceFunc = lambda c, n, op, SS, cl: {
    "char": {"name": n.get("val"), "sprites": SS.get("list")}
}

create_sprite: ReduceFunc = lambda f, e, p: {
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
    "createSprite": create_sprite,
    "prepareResult": prepare_result,
}

json_config = reader_config("config/character_config.json")

tokens = parse_tokens(json_config)
actions = parse_actions(json_config, funcs)
goto = parse_goto(json_config)
