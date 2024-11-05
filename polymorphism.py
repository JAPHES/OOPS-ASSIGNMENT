class Cat:
    def make_sound(self):
        print("Meow!")


class Dog:
    def make_sound(self):
        print("woof!!")

def play_sound(animal):
    animal.make_sound()

# create instance of a Cat and Dog
cat = Cat()
dog = Dog()

# Demonstrate polymorphism

play_sound(cat)  # output: Meow!
play_sound(dog)  # output: woof!