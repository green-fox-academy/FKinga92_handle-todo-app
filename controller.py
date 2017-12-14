from model import ToDo
import sys

class ToDoController():

    def __init__(self):
        self.to_do = ToDo()

    def workflow(self):
        if len(sys.argv) == 1:
            self.to_do.print_usage()
        elif len(sys.argv) == 2 and sys.argv[1] == "-l":
            self.to_do.list_tasks()
        elif len(sys.argv) == 2 and sys.argv[1] == "-a":
            print("Unable to add: no task provided")
        elif sys.argv[1] == "-a":
            self.to_do.add_new_task()
        elif sys.argv[1] == "-r":
            self.to_do.remove_task()
        elif sys.argv[1] == "-c":
            self.to_do.check_task()
        else:
            print("Unsupported argument" + "\n")
            self.to_do.print_usage()


to_do = ToDoController()
to_do.workflow()
