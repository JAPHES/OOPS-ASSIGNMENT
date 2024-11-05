class Calculator:
    count = 0  # Static attribute to track method calls

    @staticmethod
    def add(a, b):
        Calculator.count += 1  # Increment count each time add() is called
        return a + b

# Using the Calculator class
result1 = Calculator.add(5, 3)
print(f"Result 1: {result1}")  # Output: Result 1: 8

result2 = Calculator.add(10, 15)
print(f"Result 2: {result2}")  # Output: Result 2: 25

# Check the count of calls to add()
print(f"Add method called: {Calculator.count} times")  # Output: Add method called: 2 times
