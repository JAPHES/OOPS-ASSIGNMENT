class Engine:
    def start(self):
        print("Engine started.")

    def stop(self):
        print("Engine stopped.")

class Car:
    def __init__(self):
        # Initialize Car with an Engine instance
        self.engine = Engine()

    def start_engine(self):
        # Use the Engine's start method
        self.engine.start()

    def stop_engine(self):
        # Use the Engine's stop method
        self.engine.stop()

# Testing the classes
car = Car()
car.start_engine()  # Output: Engine started.
car.stop_engine()   # Output: Engine stopped.
