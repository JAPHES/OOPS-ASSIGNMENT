class Animal:
    def __init__(self, eat, sleep):
        self.eat = eat
        self.sleep = sleep
    def display(self):
        print(self.eat)
        print(self.sleep)

    def details(self):
        print("I like  {}".format(self.eat))
        print("I love {}".format(self.sleep))





# dog class
class Dog(Animal):
    def __init__(self, eat, sleep, bark):
        self.eat = bark
        Animal.__init__(self, eat, sleep)

    def details(self):
        print("I also like:  {}".format(self.eat))
        print("I also love:  {}".format(self.sleep))

a = Dog("eating", "sleeping", "barking")

a.display()
a.display()