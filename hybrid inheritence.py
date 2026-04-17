class animal:
    def sound(self):
        print("animal make sound")
class mammal(animal):
    def make_sound(self):
        print("mammals make sound")
class bird:
    def makes_sound(self):
        print("birds do the sounds")
class bat(mammal,bird):
    pass
obj=bat()
obj.make_sound()
obj.sound()
obj.makes_sound()
