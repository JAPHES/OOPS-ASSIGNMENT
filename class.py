class Car:



    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Details:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}")

    # create an instance of car
my_car = Car("Toyota", "Corolla", 2020)

    #Call the display info method
my_car.display_info()




