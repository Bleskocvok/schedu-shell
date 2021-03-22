#!/usr/bin/env python3


import colorama

from database import Database
from taskinator import Taskinator

import sys


def main():
    colorama.init()

    data = Database(".data")
    data.load()
    taks = Taskinator(data)
    taks.command(sys.argv)
    data.save()

    colorama.deinit()


if __name__ == "__main__":
    main()



'''
tasks add [date]
tasks add monday
tasks add tomorrow

tasks complete [n]
tasks add-complete ""
tasks add-complete [date] ""

tasks list today
tasks list yesterday
tasks list week
tasks list month
tasks list all


tasks list global
tasks add global ""
tasks complete global [n]

tasks rewards list
tasks rewards add ""
tasks rewards claim [n]
'''

