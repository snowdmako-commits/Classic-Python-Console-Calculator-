from calculator import calculate
from utils import getFloat, getText


def main():
    try:
        while True:

            print("""
            ===== SIMPLE CALCULATOR =====

            1. Addition (+)
            2. Subtraction (-)
            3. Multiplication (*)
            4. Division (/)
            5. Power (**)
            6. Modulus (%)
            7. Exit

            =============================
            """)
            choice = getText("Choose an option: ")

            if choice is None:
                continue

            if choice == "7":
                print("Calculator closed successfully!")
                break

            operators = {
                "1": "+",
                "2": "-",
                "3": "*",
                "4": "/",
                "5": "**",
                "6": "%"
            }

            if choice not in operators:
                print("Invalid choice! Please try again.")
                continue

            num1 = getFloat("Enter first number: ")

            if num1 is None:
                continue

            num2 = getFloat("Enter second number: ")

            if num2 is None:
                continue

            operator = operators[choice]

            result = calculate(num1, operator, num2)

            if result is not None:
                print(f"\nResult: {num1} {operator} {num2} = {result}")

    except Exception as e:
        print(f"Main Error: {e}")


if __name__ == "__main__":
    try:
        main()

    except Exception as e:
        print(f"Program Error: {e}")

