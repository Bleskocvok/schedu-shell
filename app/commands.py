
from typing import List
import colorama

from command import Command
import calendar
import database
import state
import task


def print_tasks(printer, tasks):
    for i, t in enumerate(tasks):
        cmap = {
            task.TaskState.Todo : (None, None, colorama.Style.DIM),
            task.TaskState.Finished : (colorama.Fore.GREEN, None, None),
            task.TaskState.Failed : (colorama.Fore.RED, None, None)
        }
        sym = t.state.symbol()
        printer.print_color(cmap[t.state], f" {sym} {i}   {t.state}: {t.description}")


def try_change_state(state: state.State
                    , d: str
                    , idx: str
                    , to: task.TaskState) -> task.Task:
    try:
        idx = int(idx)
    except:
        raise RuntimeError("invalid number value")
    date = calendar.parse(d)
    if date is None:
        raise RuntimeError("wrong day format")
    tasks = state.database.get_tasks(str(date))
    if idx >= len(tasks):
        raise RuntimeError("invalid task number")
    tasks[idx].state = to
    print_tasks(state, [tasks[idx]])
    return tasks[idx]


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
        self.description = "adds a task to a given day"
        self.usage = "[day] [description]"
        self.arg_num = 2

    def perform(self, state: state.State, args: List[str]):
        d = args[0]
        date = calendar.parse(d)
        if date is None:
            raise RuntimeError("wrong day format")
        t = database.Task(args[1])
        state.database.add_task(str(date), t)


class Remove(Command):
    def __init__(self):
        self.name = "remove"
        self.description = "removes a task from a given day"
        self.usage = "[day] [number]"
        self.arg_num = 2

    def perform(self, state: state.State, args: List[str]):
        d = args[0]
        date = calendar.parse(d)
        idx = 0
        try:
            idx = int(idx)
        except:
            raise RuntimeError("invalid number value")
        if date is None:
            raise RuntimeError("wrong day format")
        state.database.remove_task(str(date), idx)


class Finish(Command):
    def __init__(self):
        self.name = "finish"
        self.description = "finishes a task in a given day"
        self.usage = "[day] [number]"
        self.arg_num = 2

    def perform(self, state: state.State, args: List[str]):
        try_change_state(state, args[0], args[1], task.TaskState.Finished)


class Unfinish(Command):
    def __init__(self):
        self.name = "unfinish"
        self.description = "returns a given task to unfinished state"
        self.usage = "[day] [number]"
        self.arg_num = 2

    def perform(self, state: state.State, args: List[str]):
        try_change_state(state, args[0], args[1], task.TaskState.Todo)


class Fail(Command):
    def __init__(self):
        self.name = "fail"
        self.description = "fails a given task"
        self.usage = "[day] [number]"
        self.arg_num = 2

    def perform(self, state: state.State, args: List[str]):
        try_change_state(state, args[0], args[1], task.TaskState.Failed)


class List(Command):
    def __init__(self):
        self.name = "list"
        self.description = "lists all tasks in a given day"
        self.usage = "[day]"
        self.arg_num = 1

    def perform(self, state: state.State, args: List[str]):
        d = args[0]
        date = calendar.parse(d)
        if date is None:
            raise RuntimeError("wrong day format")
        state.print(f"{d} - tasks:")
        print_tasks(state, state.database.get_tasks(str(date)))
