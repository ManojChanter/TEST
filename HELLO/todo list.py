#Command Line Todo application

import argparse
import datetime
import os

import self as self


def getdate():
    return datetime.datetime.now()
z =getdate()
total=0
class items(object):
    """list stored as a file in / todo"""
    x=os.getcwd()
    file_location = fr"(x)\todo.txt"
    done_location = fr"(x)\done.txt"
def init(self):
    self.items = open(self.file_location, "r").readlines
    (
def listAdd(self, arg):
    print("added item: " + arg)
    with open(self.file_location, "a+") as f:
        f.writelines(arg + "\n")
def listshow(self):
    print("\n      todos\n" + "-"*75)
    if not self.items:
        print("no tasks to be done")
    else:
        for sno, item in enumerate(self.items):
            print(str(sno+1) + "." + item)
def listdelete(self, arg):
    try:
        doneTask = self.items.pop(arg - 1)
        print("completed task no." + str(arg) + " (%s), deleted todo" % doneTask.strip ()
              )
        print(f"deleted item:(arg)")
        with open(self.file_location, "w") as f:
            for item in self.items:
                f.writelines(item)
    except Exception as e:
        print(f"Error: todo (arg) does not exist")
def listdone(self,arg):
    try:
        g = self.times[arg-1]
        print(f"marked todo(arg) as done")
    )













