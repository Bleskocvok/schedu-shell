

from typing import List, Dict
from enum import Enum
import yaml


class TaskState(Enum):
    Todo = 0,
    Completed = 1,
    Failed = 2


class Task:
    def __init__(self, description: str, state: TaskState = TaskState.Todo):
        self.description = description
        self.state = state


class Database:
    def __init__(self, savefile: str):
        self.tasks: Dict[Date, List[Task]] = {}
        self.savefile = savefile

    def add_task(self, group: str, task: Task) -> None:
        if self.tasks.get(group) is None:
            self.tasks[group] = list()
        self.tasks[group].append(task)

    def remove_task(self, group: str, index: int) -> bool:
        if index >= len(self.get_tasks(group)):
            return False
        del self.tasks[group][index]
        return True

    def get_tasks(self, group: str) -> List[Task]:
        empty: List[Task] = list()
        return self.tasks.get(group, empty)

    def get_groups(self) -> List[str]:
        return self.tasks.keys()

    def load(self):
        data = {}
        try:
            with open(self.savefile, "r") as f:
                data = yaml.load(f.read(), Loader=yaml.Loader)
            self.tasks = data
        except FileNotFoundError:
            pass

    def save(self):
        with open(self.savefile, "w") as f:
            out = yaml.dump(self.tasks, Dumper=yaml.Dumper)
            f.write(out)


