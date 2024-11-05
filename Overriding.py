class Employee:
    def calculate_salary(self):
        print("Calculating generic employee salary.")

class Manager(Employee):
    def calculate_salary(self):
        # Override the method to provide a specific calculation
        base_salary = 50000
        bonus = 10000
        total_salary = base_salary + bonus
        print(f"Manager's salary: ${total_salary}")

# Demonstrate overridden behavior
employee = Employee()
manager = Manager()

# Call calculate_salary on both objects
employee.calculate_salary()  # Output: Calculating generic employee salary.
manager.calculate_salary()    # Output: Manager's salary: $60000
