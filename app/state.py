

from typing import Any, Dict, Tuple
import colorama

import database


class State:
    def __init__(self, cmd_map: Dict[str, Any], database: database.Database):
        self.cmd_map = cmd_map
        self.database = database

    def print(self, *args, **kwargs):
        print(*args, **kwargs)

    def print_color(self, color: Tuple[Any, Any, Any], *args, **kwargs):
        fg, bg, style = color
        if fg is not None:
            print(fg, end="")
        if bg is not None:
            print(bg, end="")
        if style is not None:
            print(style, end="")
        print(*args, **kwargs)
        print(colorama.Style.RESET_ALL, end="")
