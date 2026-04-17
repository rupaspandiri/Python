class Employ:
    def _init_(self, name):
        self.name = name

    def work(self):
        print("Employees do the work")

class Manager(Employ):
    def work(self):
        print(self.name, "the manager manages the team")

class Tester(Employ):
    def work(self):
        print(self.name, "the tester tests the code")

def employ_details(emp):
    emp.work()

m = Manager("Girls")
t = Tester("Boys")

employ_details(m)
employ_details(t)
