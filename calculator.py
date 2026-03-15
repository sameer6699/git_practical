"""
Simple Calculator - Python OOP Demo
A basic calculator using Object-Oriented Programming concepts.
"""


class Calculator:
    """A calculator that performs basic arithmetic operations."""

    def __init__(self):
        """Initialize the calculator with a result tracker."""
        self._result = 0  # Encapsulation: protected attribute

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
    print("5. Exit\n")

    while True:
        choice = input("Enter choice (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Try again.\n")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.\n")
            continue

        if choice == "1":
            print(f"Result: {calc.add(num1, num2)}\n")
        elif choice == "2":
            print(f"Result: {calc.subtract(num1, num2)}\n")
        elif choice == "3":
            print(f"Result: {calc.multiply(num1, num2)}\n")
        elif choice == "4":
            try:
                print(f"Result: {calc.divide(num1, num2)}\n")
            except ValueError as e:
                print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
