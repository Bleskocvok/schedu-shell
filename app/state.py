

from typing import Any, Dict
import colorama

import database


class State:
    def __init__(self, cmd_map: Dict[str, Any], database: database.Database):
        self.cmd_map = cmd_map
        self.database = database

    def print(self, *args, **kwargs):
        print(*args, **kwargs)
