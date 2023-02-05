#!/usr/bin/env python3
from argparse import ArgumentParser
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

HIDDEN_FILES_PREFIX = "."
FILE_OPEN_MODE = ("r", "w")
FILE_ENCODING = "utf-8"
LINE_BREAK_REPLACE = ("\n", "")
COLOR_REPLACE_STRING = "\x1b[{0!s}m"
ANSI_MAPPING = {
    "30": '<span style="color:#000000">',
    "31": '<span style="color:#ff0000">',
    "32": '<span style="color:#00ff00">',
    "33": '<span style="color:#ffff00">',
    "34": '<span style="color:#0000ff">',
    "35": '<span style="color:#ff00ff">',
    "36": '<span style="color:#00ffff">',
    "37": '<span style="color:#ffffff">',
    "0": '</span>'
}
TEMPLATES_DIR = Path(__file__).parent.resolve(strict=True) / "templates"
MAIN_TEMPLATE_NAME = "index.j2"
OUTPUT_FILENAME = Path("index.html")

def cli():
    parser = ArgumentParser(
        "pages",
        description="Generates a page based on the repository contents.",
        add_help=True
    )
    parser.add_argument(
        "repo_root",
        action="store",
        type=Path,
        metavar="PATH",
        help=(
            "Path to the repository root. "
            "The same path will be used to generate an output page."
        )
    )
    return parser.parse_args().repo_root.resolve(strict=True)

def handle_ansi_escape_codes(line:str):
    for code, color in ANSI_MAPPING.items():
        line = line.replace(COLOR_REPLACE_STRING.format(code), color)
    line = line.replace(*LINE_BREAK_REPLACE)
    return line

def load_file(file):
    with open(file, FILE_OPEN_MODE[0], encoding=FILE_ENCODING) as fd:
        content = fd.readlines()
    return tuple(handle_ansi_escape_codes(line) for line in content)

def read_repository_contents(directory):
    tree = {}
    for item in sorted(directory.iterdir()):
        if not item.is_dir() or item.name[0] == HIDDEN_FILES_PREFIX:
            continue
        tree.setdefault(
            item.name,
            tuple((file.name, load_file(file)) for file in sorted(item.iterdir()) if file.is_file())
        )
    return tree

def render(ctx):
    env: Environment = Environment(loader=FileSystemLoader(TEMPLATES_DIR, encoding=FILE_ENCODING))
    template = env.get_template(MAIN_TEMPLATE_NAME)
    html = template.render(ctx)
    with open(OUTPUT_FILENAME, FILE_OPEN_MODE[1], encoding=FILE_ENCODING) as fd:
        fd.write(html)

if __name__ == "__main__":
    working_directory = cli()
    context = {"distros": read_repository_contents(working_directory)}
    render(context)
    exit(0)