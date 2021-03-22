
from typing import List, Dict, Any

from database import Database
import commands
import state


def transform_quotes(args: List[str]) -> List[str]:
    i = 0
    while i < len(args):
        found = args[i].find('"')
        args[i] = args[i].replace('"', '', 1)
        if found == -1:
            i += 1
            continue
        j = i
        while j < len(args) and args[j].find('"') == -1:
            j += 1
        for _ in range(j - i):
            if i+1 >= len(args):
                break
            args[i+1] = args[i+1].replace('"', '', 1)
            args[i] = args[i] + args[i+1]
            del args[i+1]
        i += 1


class Taskinator:
    def __init__(self, database: Database):
        cmd_map: Dict[str, Any] = {}
        for (name, val) in commands.__dict__.items():
            if not isinstance(val, type):
                continue
            inst = val()
            if (isinstance(inst, commands.Command)
                    and type(inst) is not commands.Command):
                cmd_map[inst.name] = inst
        self.state = state.State(cmd_map, database)

    def command(self, args: List[str]):
        transform_quotes(args)
        if len(args) < 2:
            self.state.print(f"ERROR: no argument, try:\n    {args[0]} help")
            return
        cmd = args[1]
        if cmd not in self.state.cmd_map:
            self.state.print("ERROR: wrong arg")
            return
        if len(args) - 2 < self.state.cmd_map[cmd].arg_num:
            return
        try:
            self.state.cmd_map[cmd].perform(self.state, args[2:])
        except Exception as ex:
            self.state.print("ERROR:", ex)


