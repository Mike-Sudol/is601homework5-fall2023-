from app.commands import Command
from app.calculator import Calculator
from decimal import Decimal, InvalidOperation

class SubtractCommand(Command):
    ''' Command for Subtraction'''

    def execute(self, args):
        ''' Subtract 2 Numbers, Prints the output'''
        try: 
            number1 = Decimal(args[0])
            number2 = Decimal(args[1]) 
        except InvalidOperation:
            print("Error: Invalid number format. Please enter valid decimal numbers.")
            return None

        result = Calculator.subtract(number1, number2)
        print(f"The result of {number1} - {number2} is: {result}")
        return result
