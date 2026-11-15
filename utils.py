def getFloat(message):
    try:
        number = float(input(message))
        return number

    except ValueError:
        print("Error: Please enter a valid number!")
        return None

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None


def getChoice(message):
    try:
        choice = input(message).strip()

        if choice == "":
            raise ValueError("Input cannot be empty!")

        return choice

    except ValueError as e:
        print(f"Error: {e}")
        return None