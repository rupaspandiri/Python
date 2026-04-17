class mother:
    def parent(self):
        print("this is base class")
class child(mother):
        def parent(self):
            print("this is child class")
ch=child()
ch.parent()

 
class animal:
    def make_sound(self):
        print("animals make sound")
class dog(animal):
    def make_sound(self):
        print("dog makes sound bow ")
class cat(animal):
    def makes_sound(self):
        print("cat makes sound meow")
obj=cat()
obj.make_sound()

