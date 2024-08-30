import argparse
import sys

taskFile = 'tasks.txt'

def addTask(taskDesc):
    with open(taskFile, 'a') as file:
        file.write(taskDesc + '\n')
    print(f"Task added: {taskDesc}")

def showTasks():
    try:
        with open(taskFile, 'r') as file:
            tasks = file.readlines()
            if tasks:
                print("Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
            else:
                print("No tasks found.")
    except FileNotFoundError:
        print("No tasks found.")

def completeTask(taskNum):
    try:
        with open(taskFile, 'r') as file:
            tasks = file.readlines()
        if 0 < taskNum <= len(tasks):
            tasks.pop(taskNum - 1)
            with open(taskFile, 'w') as file:
                file.writelines(tasks)
            print(f"Task {taskNum} completed.")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks found.")

def deleteTask(taskNum):
    try:
        with open(taskFile, 'r') as file:
            tasks = file.readlines()
        if 0 < taskNum <= len(tasks):
            del tasks[taskNum - 1]
            with open(taskFile, 'w') as file:
                file.writelines(tasks)
            print(f"Task {taskNum} deleted.")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("No tasks found.")

def main():
    parser = argparse.ArgumentParser(description='Task Manager CLI')
    parser.add_argument('command', type=str, choices=['add', 'show', 'complete', 'delete'],
                        help='Command to execute')
    parser.add_argument('arguments', nargs='*', help='Arguments for the command')
    args = parser.parse_args()

    if args.command == 'add':
        if args.arguments:
            addTask(' '.join(args.arguments))
        else:
            print("No task description provided.")
    elif args.command == 'show':
        showTasks()
    elif args.command == 'complete':
        if args.arguments:
            completeTask(int(args.arguments[0]))
        else:
            print("No task number provided.")
    elif args.command == 'delete':
        if args.arguments:
            deleteTask(int(args.arguments[0]))
        else:
            print("No task number provided.")

if __name__ == '__main__':
    main()
