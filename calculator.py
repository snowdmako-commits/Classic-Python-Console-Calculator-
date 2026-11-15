def add(a, b):
    try:
        return a + b

    except Exception as e:
        print(f"Addition Error: {e}")
        return None


def subtract(a, b):
    try:
        return a - b

    except Exception as e:
        print(f"Subtraction Error: {e}")
        return None


def multiply(a, b):
    try:
        return a * b

    except Exception as e:
        print(f"Multiplication Error: {e}")
        return None


def divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None

    except Exception as e:
        print(f"Division Error: {e}")
        return None


def power(a, b):
    try:
        return a ** b

    except Exception as e:
        print(f"Power Error: {e}")
        return None


def mod(a, b):
    try:
        return a % b

    except ZeroDivisionError:
        print("Error: Cannot calculate modulus by zero!")
        return None

    except Exception as e:
        print(f"Modulus Error: {e}")
        return None


def calculate(a, operator, b):
    try:
        if operator == "+":
            return add(a, b)

        elif operator == "-":
            return subtract(a, b)

        elif operator == "*":
            return multiply(a, b)

        elif operator == "/":
            return divide(a, b)

        elif operator == "**":
            return power(a, b)

        elif operator == "%":
            return mod(a, b)

        else:
            raise ValueError("Invalid operator!")

    except ValueError as e:
        print(f"Calculation Error: {e}")
        return None

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None
