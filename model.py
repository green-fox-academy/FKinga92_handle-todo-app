import sys

class ToDo(object):

    def __init__(self):
        with open("usage.txt", "r") as manual:
            self.usage = manual.read()
        with open("my_todos.txt", "r") as my_file:
            self.content = my_file.readlines()    

    def print_usage(self):
        print(self.usage)

    def list_tasks(self):
        if not self.content:
            print("No todos for today! :)")
        else:
            for index, line in enumerate(self.content):
                print(str(index + 1) + " - " + line.rstrip())

    def add_new_task(self):
        with open("my_todos.txt", "a") as my_file:
            if not self.content:
                my_file.write("[ ] " + str(sys.argv[2]))
            else:
                my_file.write("\n" + "[ ] " + str(sys.argv[2]))

    def remove_task(self):
        if int(sys.argv[2]) <= len(self.content) and len(self.content) >= 2:
            self.content.remove(self.content[int(sys.argv[2]) - 1])
            self.update_file()
        else:
            print("Unable to remove: index is out of bound")

    def check_task(self):
        if int(sys.argv[2]) <= len(self.content):
            index_of_completed = int(sys.argv[2])
            for i in range(len(self.content)):
                if i == index_of_completed - 1:
                    self.content[i] = "[x]" + self.content[i][3: ]
            self.update_file()
        else:
            print("Unable to remove: index is out of bound")

    def update_file(self):
        updated_file = open("my_todos.txt", "w")
        for i in range(len(self.content)):
            if i < len(self.content) - 1:
                updated_file.write(self.content[i])
            else:
                updated_file.write(self.content[i].rstrip())
        updated_file.close()
