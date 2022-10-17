import pprint

from config import character, scene
from lrparser import Parser, Tokenizer
from lrparser.utils.action_table_descriptor import ActionTableDescriptor
from lrparser.utils.goto_table_descriptor import GotoTableDescriptor

tokenizer = Tokenizer(scene.tokens)
parser = Parser(
    ActionTableDescriptor(scene.actions),
    GotoTableDescriptor(scene.goto),
)

file = 'scene_1.txt'
with open(f'config/tmp/script/{file}', 'r') as f:
    text = f.read()

x = tokenizer.tokenize(text)
# pprint.pprint(x)

y  = parser.parse(x)
pprint.pprint(y)
