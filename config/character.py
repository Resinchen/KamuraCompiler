from config.reader import parse_actions, parse_goto, parse_tokens, reader_config
from lrparser.utils.table_descriptor import ReduceFunc

updateCharacterList: ReduceFunc = lambda CS, C: {
    "list": [*CS.get("list"), C.get("char")]
}
createCharacterList: ReduceFunc = lambda C1, C2: {
    "list": [C1.get("char"), C2.get("char")]
}

updateSpriteList: ReduceFunc = lambda SS, S: {
    "list": [*SS.get("list"), S.get("sprite")]
}
createSpriteList: ReduceFunc = lambda S1, S2: {
    "list": [S1.get("sprite"), S2.get("sprite")]
}

createCharacterWithoutSprites: ReduceFunc = lambda c, n: {
    "char": {"name": n.get("val")}
}
createCharacter: ReduceFunc = lambda c, n, op, SS, cl: {
    "char": {"name": n.get("val"), "sprites": SS.get("list")}
}

createSprite: ReduceFunc = lambda f, e, p: {
    "sprite": {"field": f.get("val"), "path": p.get("val")[1:-1]}
}

prepareResult: ReduceFunc = lambda CS, e: {"res": CS.get("list")}


funcs: dict[str, ReduceFunc] = {
    "updateCharacterList": updateCharacterList,
    "createCharacterList": createCharacterList,
    "updateSpriteList": updateSpriteList,
    "createSpriteList": createSpriteList,
    "createCharacterWithoutSprites": createCharacterWithoutSprites,
    "createCharacter": createCharacter,
    "createSprite": createSprite,
    "prepareResult": prepareResult,
}

json_config = reader_config("config/character_config.json")

tokens = parse_tokens(json_config)
actions = parse_actions(json_config, funcs)
goto = parse_goto(json_config)
