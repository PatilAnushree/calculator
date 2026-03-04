class Calculator:
    #constructor
    def __init__(self,first_number,operation,second_number):
        self.first_number = first_number
        self.operation = operation
        self.second_number = second_number

    def add(self):
        return self.first_number + self.second_number
    
    def subtract(self):
        return self.first_number - self.second_number
    
    def multiply(self):
        return self.first_number * self.second_number
    
    def divide(self):
        if self.second_number == 0:
            return "Error: Division by zero is not allowed."
        return self.first_number / self.second_number
    
class AdvancedCalculator(Calculator):
    def power(self):
        return self.first_number ** self.second_number
    
    def square_root(self):
        if self.first_number < 0:
            return "Error: Square root of a negative number is not allowed."
        return self.first_number ** 0.5
    
def main():
    while True:
        print("\nSimple Calculator")
        choice=input("Q => : Quit or press enter the operation: ")
        if choice.upper() == "Q":
            print("Exiting the calculator. Goodbye!")
            break
        first_number = float(input("Enter the first number: "))

        operation = input("Enter the operation (+, -, *, /,^ ,sqrt): ")
        operation = operation.lower()
        if operation != "sqrt":
            second_number = float(input("Enter the second number: "))
        else :
            second_number = 0
        
        
        calculator = AdvancedCalculator(first_number, operation, second_number)

        if calculator.operation == "+":
            result = calculator.add()

        elif calculator.operation == "-":
            result = calculator.subtract()

        elif calculator.operation == "*":
            result = calculator.multiply()

        elif calculator.operation == "/":
            result = calculator.divide()

        elif calculator.operation == "^":
            result = calculator.power()

        elif calculator.operation.lower() == "sqrt":
            result = calculator.square_root()

        elif calculator.operation.lower() == "q":
            print("Exiting the calculator. Goodbye!")
            exit()

        else:
            print("Invalid operation.")
            return
        print(f"Result: {result}")

if __name__ == "__main__":
    main()