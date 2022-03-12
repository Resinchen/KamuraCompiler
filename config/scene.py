from config.reader import parse_actions, parse_goto, parse_tokens, reader_config
from lrparser.utils.table_descriptor import ReduceFunc

prepareResult: ReduceFunc = lambda LL, AL: {
    "res": {
        "chars": LL.get("chars"),
        "files": LL.get("files"),
        "actions": AL.get("list"),
    }
}

updateLoadlist: ReduceFunc = lambda LL, L: {
    "chars": [*LL.get("chars"), L.get("char")],
    "files": [*LL.get("files"), L.get("file")],
}
createLoadlist: ReduceFunc = lambda L1, L2: {
    "chars": [L1.get("char"), L2.get("char")],
    "files": [L1.get("file"), L2.get("file")],
}

updateActionlist: ReduceFunc = lambda AL, A: {
    "list": [*AL.get("list"), A.get("action")]
}
createActionlist: ReduceFunc = lambda A1, A2: {
    "list": [A1.get("action"), A2.get("action")]
}

makeActionFromSet: ReduceFunc = lambda S: {"action": S.get("set")}
makeActionFromPlay: ReduceFunc = lambda P: {"action": P.get("play")}
makeActionFromPhrase: ReduceFunc = lambda P: {"action": P.get("phrase")}
makeActionFromChoice: ReduceFunc = lambda C: {"action": C.get("choice")}
makeActionFromVarle: ReduceFunc = lambda C: {"action": C.get("varle")}
makeActionFromJump: ReduceFunc = lambda J: {"action": J.get("jump")}
makeActionFromMark: ReduceFunc = lambda M: {"action": M.get("mark")}
makeActionFromLoadscene: ReduceFunc = lambda L: {"action": L.get("next_scene")}

createLoad: ReduceFunc = lambda l, W: {"char": W.get("char"), "file": W.get("file")}
createSet: ReduceFunc = lambda s, W: {
    "set": {"type": W.get("type"), "payload": W.get("info")}
}
createPlay: ReduceFunc = lambda p, W: {
    "play": {"type": W.get("type"), "payload": W.get("info")}
}
createPhrase: ReduceFunc = lambda l, O, s, w: {
    "phrase": {"speaker": l.get("val"), "options": O.get("opt"), "text": w.get("val")}
}
createPhraseWithoutOptions: ReduceFunc = lambda l, s, w: {
    "phrase": {"speaker": l.get("val"), "text": w.get("val")}
}
createChoice: ReduceFunc = lambda P, V: {
    "choice": {"question": P.get("phrase"), "variants": V.get("list")}
}
createVarle: ReduceFunc = lambda i, C, J: {
    "varle": {"condition": C.get("bool_list"), "target": J.get("jump")}
}
createJump: ReduceFunc = lambda j, mn: {"jump": {"markName": mn.get("val")}}
createMark: ReduceFunc = lambda m, mn: {"mark": {"markName": mn.get("val")}}
createLoadscene: ReduceFunc = lambda l, p: {"next_scene": {"pathScene": p.get("val")}}

createVarlist: ReduceFunc = lambda V: {"list": V.get("variant")}
updateVarlist: ReduceFunc = lambda VL, s, V: {
    "list": [*VL.get("list"), V.get("variant")]
}

createVariants: ReduceFunc = lambda op, VL, cl: {"list": VL.get("list")}
createVariantSingleEffect: ReduceFunc = lambda w, s, E: {
    "variant": {"text": w.get("val"), "effects": [E.get("effect")]}
}
createVariantMultiEffect: ReduceFunc = lambda w, s, EL: {
    "variant": {"text": w.get("val"), "effects": EL.get("list")}
}

createEffectList: ReduceFunc = lambda E1, c, E2: {
    "list": [E1.get("effect"), E2.get("effect")]
}
createEffectFlag: ReduceFunc = lambda f, e, b: {
    "effect": {"set_flag", f.get("val"), b.get("val")}
}
createEffectCounter: ReduceFunc = lambda cn, op, d: {
    "effect": {"change_counter", cn.get("val"), d.get("val"), op.get("val")}
}

createOptionsPosition: ReduceFunc = lambda o, p, c: {
    "opt": {"pos": p.get("val"), "emo": None}
}
createOptionsEmotion: ReduceFunc = lambda o, e, c: {
    "opt": {"pos": None, "emo": e.get("val")}
}
createOptionsPositionAndEmotion: ReduceFunc = lambda o, p, c, e, cl: {
    "opt": {"pos": p.get("val"), "emo": e.get("val")}
}

createConditionCounter: ReduceFunc = lambda cn, bo, d: {
    "boollist": {
        "type": "check_counter",
        "left": cn.get("val"),
        "op": bo.get("val"),
        "right": d.get("val"),
    }
}
createConditionFlag: ReduceFunc = lambda f, i, b: {
    "boollist": {
        "type": "check_flag",
        "left": f.get("val"),
        "op": "is",
        "right": b.get("val"),
    }
}
createConditionAnd: ReduceFunc = lambda C1, a, C2: {
    "boollist": {"left": C1.get("boollist"), "op": "and", "right": C2.get("boollist")}
}
createConditionOr: ReduceFunc = lambda C1, o, C2: {
    "boollist": {{"left": C1.get("boollist"), "op": "or", "right": C2.get("boollist")}}
}
createConditionNot: ReduceFunc = lambda n, C: {
    "boollist": {{"left": None, "op": "not", "right": C.get("boollist")}}
}

createSetBackground: ReduceFunc = lambda b, n: {
    "type": "set_background",
    "info": n.get("val"),
}
createSetText: ReduceFunc = lambda t, w: {"type": "set_text", "info": w.get("val")}
createSetBlackout: ReduceFunc = lambda b: {"type": "set_blackout"}
createPlaySound: ReduceFunc = lambda s, n: {"type": "play_sound", "info": n.get("val")}

createLoadCharacter: ReduceFunc = lambda c, n, s, l: {
    "char": {"name": n.get("val"), "label": l.get("val")}
}
createLoadImage: ReduceFunc = lambda s, p: {
    "file": {"type": "image", "path": p.get("val")}
}
createLoadSound: ReduceFunc = lambda s, p: {
    "file": {"type": "image", "path": p.get("val")}
}

funcs: dict[str, ReduceFunc] = {
    "prepareResult": prepareResult,
    "updateLoadlist": updateLoadlist,
    "createLoadlist": createLoadlist,
    "updateActionlist": updateActionlist,
    "createActionlist": createActionlist,
    "makeActionFromSet": makeActionFromSet,
    "makeActionFromPlay": makeActionFromPlay,
    "makeActionFromPhrase": makeActionFromPhrase,
    "makeActionFromChoice": makeActionFromChoice,
    "makeActionFromVarle": makeActionFromVarle,
    "makeActionFromJump": makeActionFromJump,
    "makeActionFromMark": makeActionFromMark,
    "makeActionFromLoadscene": makeActionFromLoadscene,
    "createLoad": createLoad,
    "createSet": createSet,
    "createPlay": createPlay,
    "createPhrase": createPhrase,
    "createPhraseWithoutOptions": createPhraseWithoutOptions,
    "createChoice": createChoice,
    "createVarle": createVarle,
    "createJump": createJump,
    "createMark": createMark,
    "createLoadscene": createLoadscene,
    "createVarlist": createVarlist,
    "updateVarlist": updateVarlist,
    "createVariants": createVariants,
    "createVariantSingleEffect": createVariantSingleEffect,
    "createVariantMultiEffect": createVariantMultiEffect,
    "createEffectList": createEffectList,
    "createEffectFlag": createEffectFlag,
    "createEffectCounter": createEffectCounter,
    "createOptionsPosition": createOptionsPosition,
    "createOptionsEmotion": createOptionsEmotion,
    "createOptionsPositionAndEmotion": createOptionsPositionAndEmotion,
    "createConditionCounter": createConditionCounter,
    "createConditionFlag": createConditionFlag,
    "createConditionAnd": createConditionAnd,
    "createConditionOr": createConditionOr,
    "createConditionNot": createConditionNot,
    "createSetBackground": createSetBackground,
    "createSetText": createSetText,
    "createSetBlackout": createSetBlackout,
    "createPlaySound": createPlaySound,
    "createLoadCharacter": createLoadCharacter,
    "createLoadImage": createLoadImage,
    "createLoadSound": createLoadSound,
}

json_config = reader_config("config/scene_config.json")

tokens = parse_tokens(json_config)
actions = parse_actions(json_config, funcs)
goto = parse_goto(json_config)
