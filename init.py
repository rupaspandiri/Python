class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("my name is:",self.name)
        print("age is:",self.age)
s1=student("hello",15)
s1.display()



class car:
    def __init__(self,carname,model,cost,color):
        self.carname=carname
        self.model=model
        self.cost=cost
        self.color=color
    def display(self):
        print("car name is",self.carname)
        print("car model is",self.model)
        print("car cost is",self.cost)
        print("car color is",self.color)
c1=car("audi",6,100000,"white")
c1.display()
