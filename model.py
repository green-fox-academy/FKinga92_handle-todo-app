import sys

def print_usage():
    heading = "Command Line Todo application"
    print(heading + "\n" + "=" * len(heading) + "\n" +
          "\n" + "Command line arguments:" + "\n" +
          "-l" + "  Lists all the tasks" + "\n" +
          "-a" + "  Adds a new task" + "\n" +
          "-r" + "  Removes a task" + "\n" +
          "-c" + "  Completes a task")

def list_tasks():
    try:
        with open("my_todos.txt", "r") as my_file:
            content = my_file.readlines()
            if not content:
                print("No todos for today! :)")
            else:
                for index, line in enumerate(content):
                    print(str(index + 1) + " - " + line.rstrip())
    except IOError:
        print("Cannot read file: my_todos.txt")

def add_new_task():
    with open("my_todos.txt", "a") as my_file:
        my_file.write("\n" + str(sys.argv[2]))
