
from typing import List

import database
from command import Command
import state
import calendar


class Help(Command):
    def __init__(self):
        self.name = "help"
        self.description = "shows help"
        self.usage = ""
        self.arg_num = 0

    def perform(self, state: state.State, args: List[str]):
        m = max([len(val.name) for (_, val) in state.cmd_map.items()])
        pad = 6
        for key, val in state.cmd_map.items():
            state.print(f"{key}".ljust(m + pad) + f"| {val.description}")


class Add(Command):
    def __init__(self):
        self.name = "add"
        self.description = ""
        self.usage = "[day] [description]"
        self.arg_num = 2

    def perform(self, state: state.State, args: List[str]):
        d = args[0]
        date = calendar.parse(d)
        if date is None:
            raise RuntimeError("wrong day format")
        t = database.Task(args[1])
        state.database.add_task(str(date), t)


class List(Command):
    def __init__(self):
        self.name = "list"
        self.description = ""
        self.usage = "[day]"
        self.arg_num = 1

    def perform(self, state: state.State, args: List[str]):
        d = args[0]
        date = calendar.parse(d)
        if date is None:
            raise RuntimeError("wrong day format")
        state.print(state.database.get_tasks(str(date)))


class Complete(Command):
    def __init__(self):
        self.name = "complete"
        self.description = ""
        self.usage = "[day] [number]"
        self.arg_num = 2

    def perform(self, state: state.State, args: List[str]):
        pass
        # d = args[0]
        # idx = args[1]
        # date = calendar.parse(d)
        # if date is None:
        #     raise RuntimeError("wrong day format")
        # tasks = state.database.get_tasks(str(date), t)
        # if idx >= len(tasks):
        #     raise RuntimeError("invalid task number")
        # tasks[idx].state = TaskState.Completed
