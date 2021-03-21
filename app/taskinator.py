
from typing import List, Dict, Any

from database import Database
import commands
import state


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


