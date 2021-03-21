

from typing import List

import state

class Command:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.usage = ""
        self.arg_num = 0

    def perform(self, state: state.State, args: List[str]) -> None:
        pass
