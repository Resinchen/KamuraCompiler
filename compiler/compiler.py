import os

from lrparser import Parser, Tokenizer
from config import character, scene
from lrparser.utils.parser import Attribute
from os import path

import json

class ParserBlock:
    def __init__(self, tokens, actions, goto):
        self.tokenizer = Tokenizer(tokens)
        self.parser = Parser(actions, goto)

class Compiler:
    def __init__(self):
        self.parsers: dict[str, ParserBlock] = {
            'char': ParserBlock(character.tokens, character.actions, character.goto),
            'scene': ParserBlock(scene.tokens, scene.actions, scene.goto)
        }

    def build_game(self, game_directory: str):
        script_folder = path.join(game_directory, 'script')
        compiled_folder = path.join(game_directory, 'compiled')
        character_file, scene_files = self._get_files(script_folder)

        if not os.path.exists(compiled_folder):
            os.makedirs(compiled_folder)

        self._compile_character_file(character_file, compiled_folder)
        for file in scene_files:
            self._compile_scene_file(file, compiled_folder)

    def _get_files(self, script_path: str) -> tuple[str, list[str]]:
        get_abspath = lambda fp: path.join(path.abspath(script_path), fp)
        filenames = os.listdir(script_path)
        filenames = [get_abspath(filepath) for filepath in filenames]

        char_filename = [filename for filename in filenames if 'chars'in filename][0]
        scene_filenames = [filename for filename in filenames if filename != char_filename]

        return char_filename, scene_filenames

    def _compile_character_file(self, filepath: str, output_folder: str) -> None:
        output_filepath = path.abspath(path.join(output_folder, path.basename(filepath).replace('.txt', '.json')))
        result = self._compile_file('char', filepath)

        with open(output_filepath, 'w+') as f:
            json.dump(result, f)

    def _compile_scene_file(self, filepath: str, output_folder: str) -> None:
        output_filepath = path.abspath(path.join(output_folder, path.basename(filepath).replace('.txt', '.json')))
        result = self._compile_file('scene', filepath)

        with open(output_filepath, 'w+') as f:
            json.dump(result, f)

    def _compile_file(self, type_file: str, filepath:str) -> Attribute:
        with open(filepath, 'r') as f:
            tokenized = self.parsers[type_file].tokenizer.tokenize(f.read())
        return self.parsers[type_file].parser.parse(tokenized)
