import json
from os import path
from pathlib import Path

from lrparser import Parser, Tokenizer
from lrparser.utils.parser import Attribute


class ParserBlock:
    def __init__(self, tokens, actions, goto):
        self.tokenizer = Tokenizer(tokens)
        self.parser = Parser(actions, goto)


class Compiler:
    def __init__(self):
        self.parsers: dict[str, ParserBlock] = {
            'char': ParserBlock(None, None, None),
            'scene': ParserBlock(None, None, None),
        }

    def build_game(self, game_directory: Path):
        script_folder = game_directory / 'script'
        compiled_folder = game_directory / 'compiled'
        character_file, scene_files = self._get_files(script_folder)

        if not compiled_folder.exists():
            compiled_folder.mkdir()

        self._compile_character_file(character_file, compiled_folder)
        for file in scene_files:
            self._compile_scene_file(file, compiled_folder)

    def _get_files(self, script_path: Path) -> tuple[Path, list[Path]]:
        filenames = [script_path.absolute() / filepath for filepath in script_path.iterdir()]

        char_filename = [filename for filename in filenames if 'chars' in filename][0]
        scene_filenames = [filename for filename in filenames if filename != char_filename]

        return char_filename, scene_filenames

    def _compile_character_file(self, filepath: Path, output_folder: Path) -> None:
        output_filepath = path.abspath(output_folder / path.basename(filepath).replace('.txt', '.json'))
        result = self._compile_file('char', filepath)

        with open(output_filepath, 'w+') as f:
            json.dump(result, f)

    def _compile_scene_file(self, filepath: Path, output_folder: Path) -> None:
        output_filepath = path.abspath(path.join(output_folder, path.basename(filepath).replace('.txt', '.json')))
        result = self._compile_file('scene', filepath)

        with open(output_filepath, 'w+') as f:
            json.dump(result, f)

    def _compile_file(self, type_file: str, filepath: Path) -> Attribute:
        with open(filepath, 'r') as f:
            tokenized = self.parsers[type_file].tokenizer.tokenize(f.read())
        return self.parsers[type_file].parser.parse(tokenized)


def get_player_file(actions):
    player_file = {}
    for action in actions:
        if action.type == 'show_choice':
            for variant in action.variants:
                player_file.setdefault(variant.effect.conter, 0)
