class string_function:
    def __init__(self, string ):
        self.string = string
    def getString(self):
        self.string=str(input())
    def printString(self):
        print(self.string.upper())

task=string_function
task.getString(task)
task.printString(task)