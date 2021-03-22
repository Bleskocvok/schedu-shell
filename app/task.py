
from enum import Enum


class TaskState(Enum):
    Todo = 0,
    Finished = 1,
    Failed = 2

    def __str__(self):
        if self == TaskState.Todo:
            return "TODO"
        if self == TaskState.Finished:
            return "DONE"
        return "FAIL"

    def symbol(self):
        if self == TaskState.Todo:
            return "*"
        if self == TaskState.Finished:
            return "+"
        return "-"


class Task:
    def __init__(self, description: str, state: TaskState = TaskState.Todo):
        self.description = description
        self.state = state

    def __str__(self):
        return f"{self.state}: {self.description}"
