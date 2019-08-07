import os
import requests
from string import Template
import urllib
import pickledb

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Todo List \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_task():
    name = input('Enter task: ')
    return name


def store_task(task):
    if task:
        auto_dump = True
        db = pickledb.load('tasks.db', auto_dump)
        db.set(task, False)
        # db.dump()


def print_tasks(tasks):
    print('Tasks: ')
    for task in tasks:
        print(task)


def get_tasks():
    auto_dump = True
    db = pickledb.load('tasks.db', auto_dump)
    return db.getall()


def delete_task(task):
    auto_dump = True
    db = pickledb.load('tasks.db', auto_dump)
    if task and db.exists(task):
        db.rem(task)
        db.dump()
    

if __name__ == "__main__":
    print_header()
    task = get_task()
    while task:
        store_task(task)
        task = get_task()
    
    print()
    tasks = get_tasks()
    print_tasks(tasks)
   
    print('\nDelete task')
    task = get_task()
    while task:
        delete_task(task)
        task = get_task()
    
    print()
    tasks = get_tasks()
    print_tasks(tasks)
    
