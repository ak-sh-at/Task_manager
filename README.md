This is a simple command-line interface (CLI) for managing tasks using a text file. The script allows you to add, show, complete, and delete tasks, all stored in a tasks.txt file.

FEATURES

1) Add Task: Add a new task to the task list.
2) Show Tasks: Display all tasks in the task list.
3) Complete Task: Mark a task as complete by removing it from the list.
4) Delete Task: Remove a task from the task list.

USAGE

The script can be run from the command line with different commands. Below are the details on how to use each command.

1) To add a task to the list, use the add command followed by the task description:<br/>
   python task.py add "Your task description here"

2) To list all tasks in the task list, use the show command: <br/>
   python task.py show

3) To mark a task as complete (i.e., remove it from the list), use the complete command followed by the task number:<br/>
   python task.py complete <task_number>

4) To delete a task from the list, use the delete command followed by the task number:<br/>
   python task.py delete <task_number>



