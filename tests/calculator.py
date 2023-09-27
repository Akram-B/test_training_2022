# mymodule.py

import statistics


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return self.add(a, -b)  # Refactoring: Call the add method to perform subtraction

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return self.multiply(a, 1 / b)  # Refactoring: Call the multiply method to perform division

    def average(self, values):
        return statistics.mean(values)


