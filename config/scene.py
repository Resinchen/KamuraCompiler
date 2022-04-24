from config.reader import parse_actions, parse_goto, parse_tokens, reader_config
from lrparser.utils.table_descriptor import ReduceFunc

prepare_result: ReduceFunc = lambda LL, AL: {
    "res": {
        "chars": LL.get("chars"),
        "files": LL.get("files"),
        "actions": AL.get("list"),
    }
}

update_loadlist: ReduceFunc = lambda LL, L: {
    "chars": [*LL.get("chars"), L.get("char")],
    "files": [*LL.get("files"), L.get("file")],
}
create_loadlist: ReduceFunc = lambda L1, L2: {
    "chars": [L1.get("char"), L2.get("char")],
    "files": [L1.get("file"), L2.get("file")],
}

update_actionlist: ReduceFunc = lambda AL, A: {
    "list": [*AL.get("list"), A.get("action")]
}
create_actionlist: ReduceFunc = lambda A1, A2: {
    "list": [A1.get("action"), A2.get("action")]
}

make_action_from_set: ReduceFunc = lambda S: {"action": S.get("set")}
make_action_from_play: ReduceFunc = lambda P: {"action": P.get("play")}
make_action_from_phrase: ReduceFunc = lambda P: {"action": P.get("phrase")}
make_action_from_choice: ReduceFunc = lambda C: {"action": C.get("choice")}
make_action_from_varle: ReduceFunc = lambda C: {"action": C.get("varle")}
make_action_from_jump: ReduceFunc = lambda J: {"action": J.get("jump")}
make_action_from_mark: ReduceFunc = lambda M: {"action": M.get("mark")}
make_action_from_loadscene: ReduceFunc = lambda L: {"action": L.get("next_scene")}

create_load: ReduceFunc = lambda l, W: {"char": W.get("char"), "file": W.get("file")}
create_set: ReduceFunc = lambda s, W: {
    "set": {"type": W.get("type"), "payload": W.get("info")}
}
create_play: ReduceFunc = lambda p, W: {
    "play": {"type": W.get("type"), "payload": W.get("info")}
}
create_phrase: ReduceFunc = lambda l, O, s, w: {
    "phrase": {"speaker": l.get("val"), "options": O.get("opt"), "text": w.get("val")}
}
create_phrase_without_options: ReduceFunc = lambda l, s, w: {
    "phrase": {"speaker": l.get("val"), "text": w.get("val")}
}
create_choice: ReduceFunc = lambda P, V: {
    "choice": {"question": P.get("phrase"), "variants": V.get("list")}
}
create_varle: ReduceFunc = lambda i, C, J: {
    "varle": {"condition": C.get("bool_list"), "target": J.get("jump")}
}
create_jump: ReduceFunc = lambda j, mn: {"jump": {"markName": mn.get("val")}}
create_mark: ReduceFunc = lambda m, mn: {"mark": {"markName": mn.get("val")}}
create_loadscene: ReduceFunc = lambda l, p: {"next_scene": {"pathScene": p.get("val")}}

create_varlist: ReduceFunc = lambda V: {"list": V.get("variant")}
update_varlist: ReduceFunc = lambda VL, s, V: {
    "list": [*VL.get("list"), V.get("variant")]
}

create_variants: ReduceFunc = lambda op, VL, cl: {"list": VL.get("list")}
create_variant_single_effect: ReduceFunc = lambda w, s, E: {
    "variant": {"text": w.get("val"), "effects": [E.get("effect")]}
}
create_variant_multi_effect: ReduceFunc = lambda w, s, EL: {
    "variant": {"text": w.get("val"), "effects": EL.get("list")}
}

create_effect_list: ReduceFunc = lambda E1, c, E2: {
    "list": [E1.get("effect"), E2.get("effect")]
}
create_effect_flag: ReduceFunc = lambda f, e, b: {
    "effect": {"set_flag", f.get("val"), b.get("val")}
}
create_effect_counter: ReduceFunc = lambda cn, op, d: {
    "effect": {"change_counter", cn.get("val"), d.get("val"), op.get("val")}
}

create_options_position: ReduceFunc = lambda o, p, c: {
    "opt": {"pos": p.get("val"), "emo": None}
}
create_options_emotion: ReduceFunc = lambda o, e, c: {
    "opt": {"pos": None, "emo": e.get("val")}
}
create_options_position_and_emotion: ReduceFunc = lambda o, p, c, e, cl: {
    "opt": {"pos": p.get("val"), "emo": e.get("val")}
}

create_condition_counter: ReduceFunc = lambda cn, bo, d: {
    "boollist": {
        "type": "check_counter",
        "left": cn.get("val"),
        "op": bo.get("val"),
        "right": d.get("val"),
    }
}
create_condition_flag: ReduceFunc = lambda f, i, b: {
    "boollist": {
        "type": "check_flag",
        "left": f.get("val"),
        "op": "is",
        "right": b.get("val"),
    }
}
create_condition_and: ReduceFunc = lambda C1, a, C2: {
    "boollist": {"left": C1.get("boollist"), "op": "and", "right": C2.get("boollist")}
}
create_condition_or: ReduceFunc = lambda C1, o, C2: {
    "boollist": {{"left": C1.get("boollist"), "op": "or", "right": C2.get("boollist")}}
}
create_condition_not: ReduceFunc = lambda n, C: {
    "boollist": {{"left": None, "op": "not", "right": C.get("boollist")}}
}

create_set_background: ReduceFunc = lambda b, n: {
    "type": "set_background",
    "info": n.get("val"),
}
create_set_text: ReduceFunc = lambda t, w: {"type": "set_text", "info": w.get("val")}
create_set_blackout: ReduceFunc = lambda b: {"type": "set_blackout"}
create_play_sound: ReduceFunc = lambda s, n: {
    "type": "play_sound",
    "info": n.get("val"),
}

create_load_character: ReduceFunc = lambda c, n, s, l: {
    "char": {"name": n.get("val"), "label": l.get("val")}
}
create_load_image: ReduceFunc = lambda s, p: {
    "file": {"type": "image", "path": p.get("val")}
}
create_load_sound: ReduceFunc = lambda s, p: {
    "file": {"type": "image", "path": p.get("val")}
}

funcs: dict[str, ReduceFunc] = {
    "prepareResult": prepare_result,
    "updateLoadlist": update_loadlist,
    "createLoadlist": create_loadlist,
    "updateActionlist": update_actionlist,
    "createActionlist": create_actionlist,
    "makeActionFromSet": make_action_from_set,
    "makeActionFromPlay": make_action_from_play,
    "makeActionFromPhrase": make_action_from_phrase,
    "makeActionFromChoice": make_action_from_choice,
    "makeActionFromVarle": make_action_from_varle,
    "makeActionFromJump": make_action_from_jump,
    "makeActionFromMark": make_action_from_mark,
    "makeActionFromLoadscene": make_action_from_loadscene,
    "createLoad": create_load,
    "createSet": create_set,
    "createPlay": create_play,
    "createPhrase": create_phrase,
    "createPhraseWithoutOptions": create_phrase_without_options,
    "createChoice": create_choice,
    "createVarle": create_varle,
    "createJump": create_jump,
    "createMark": create_mark,
    "createLoadscene": create_loadscene,
    "createVarlist": create_varlist,
    "updateVarlist": update_varlist,
    "createVariants": create_variants,
    "createVariantSingleEffect": create_variant_single_effect,
    "createVariantMultiEffect": create_variant_multi_effect,
    "createEffectList": create_effect_list,
    "createEffectFlag": create_effect_flag,
    "createEffectCounter": create_effect_counter,
    "createOptionsPosition": create_options_position,
    "createOptionsEmotion": create_options_emotion,
    "createOptionsPositionAndEmotion": create_options_position_and_emotion,
    "createConditionCounter": create_condition_counter,
    "createConditionFlag": create_condition_flag,
    "createConditionAnd": create_condition_and,
    "createConditionOr": create_condition_or,
    "createConditionNot": create_condition_not,
    "createSetBackground": create_set_background,
    "createSetText": create_set_text,
    "createSetBlackout": create_set_blackout,
    "createPlaySound": create_play_sound,
    "createLoadCharacter": create_load_character,
    "createLoadImage": create_load_image,
    "createLoadSound": create_load_sound,
}

json_config = reader_config("config/scene_config.json")

tokens = parse_tokens(json_config)
actions = parse_actions(json_config, funcs)
goto = parse_goto(json_config)
