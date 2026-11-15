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
