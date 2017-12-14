import sys

class ToDo(object):

    def __init__(self):
        with open("usage.txt", "r") as manual:
            self.usage = manual.read()

    def print_usage(self):
        print(self.usage)

    def list_tasks(self):
        with open("my_todos.txt", "r") as my_file:
            content = my_file.readlines()
            if not content:
                print("No todos for today! :)")
            else:
                for index, line in enumerate(content):
                    print(str(index + 1) + " - " + line.rstrip())

    def add_new_task(self):
        with open("my_todos.txt", "a") as my_file:
            my_file.write("\n" + str(sys.argv[2]))
    
    def remove_task(self):
        my_file = open("my_todos.txt", "r")
        content = my_file.readlines()
        my_file.close()
        if len(content) > 2:
            content.remove(content[int(sys.argv[2]) - 1])
        updated_file = open("my_todos.txt", "w")
        for i in range(len(content)):
            if i < len(content) - 1:
                updated_file.write(content[i])
            else:
                updated_file.write(content[i].rstrip())
        updated_file.close()
        
    def check_task(self):
        my_file = open("my_todos.txt", "r")
        content = my_file.readlines()
        my_file.close()
        index_of_completed = int(sys.argv[2])
        for i in range(len(content)):
            if i == index_of_completed - 1:
                content[i] = "[x]" + content[i][3: ]
        updated_file = open("my_todos.txt", "w")
        for i in range(len(content)):
            if i < len(content) - 1:
                updated_file.write(content[i])
            else:
                updated_file.write(content[i].rstrip())
        updated_file.close()
