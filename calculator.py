"""
Simple Calculator - Python OOP Demo
A basic calculator using Object-Oriented Programming concepts.
"""
import math


class Calculator:
    """A calculator that performs basic arithmetic operations."""

    def __init__(self):
        """Initialize the calculator with a result tracker."""
        self._result = 0  # Encapsulation: protected attribute
        self._history = []
        self._history_index = 0
        self._history_limit = 10
        self._history_position = 0

    def add(self, a: float, b: float) -> float:
        """Return the sum of a and b."""
        self._result = a + b
        return self._result

    def subtract(self, a: float, b: float) -> float:
        """Return the difference (a - b)."""
        self._result = a - b
        return self._result

    def multiply(self, a: float, b: float) -> float:
        """Return the product of a and b."""
        self._result = a * b
        return self._result

    def divide(self, a: float, b: float) -> float:
        """Return a divided by b. Raises ValueError if b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self._result = a / b
        return self._result

    def power(self, base: float, exponent: float) -> float:
        """Return base raised to the power of exponent."""
        self._result = base ** exponent
        return self._result

    def modulo(self, a: float, b: float) -> float:
        """Return the remainder of a divided by b. Raises ValueError if b is zero."""
        if b == 0:
            raise ValueError("Cannot modulo by zero")
        self._result = a % b
        return self._result

    def square_root(self, x: float) -> float:
        """Return the square root of x. Raises ValueError if x is negative."""
        if x < 0:
            raise ValueError("Cannot take square root of a negative number")
        self._result = math.sqrt(x)
        return self._result

    def absolute(self, x: float) -> float:
        """Return the absolute value of x."""
        self._result = abs(x)
        return self._result

    @property
    def result(self) -> float:
        """Return the last computed result (encapsulation)."""
        return self._result

    def reset(self) -> None:
        """Reset the stored result to zero."""
        self._result = 0


def main():
    """Demo the calculator in a simple menu-driven way."""
    calc = Calculator()

    print("=== Simple Calculator (OOP) ===\n")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (x^y)")
    print("6. Modulo (remainder)")
    print("7. Square root")
    print("8. Absolute value")
    print("9. Exit\n")

    while True:
        choice = input("Enter choice (1-9): ").strip()

        if choice == "9":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4", "5", "6", "7", "8"):
            print("Invalid choice. Try again.\n")
            continue

        try:
            if choice in ("7", "8"):
                num1 = float(input("Enter number: "))
                num2 = 0  # not used
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.\n")
            continue

        try:
            if choice == "1":
                print(f"Result: {calc.add(num1, num2)}\n")
            elif choice == "2":
                print(f"Result: {calc.subtract(num1, num2)}\n")
            elif choice == "3":
                print(f"Result: {calc.multiply(num1, num2)}\n")
            elif choice == "4":
                print(f"Result: {calc.divide(num1, num2)}\n")
            elif choice == "5":
                print(f"Result: {calc.power(num1, num2)}\n")
            elif choice == "6":
                print(f"Result: {calc.modulo(num1, num2)}\n")
            elif choice == "7":
                print(f"Result: {calc.square_root(num1)}\n")
            elif choice == "8":
                print(f"Result: {calc.absolute(num1)}\n")
        except ValueError as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
