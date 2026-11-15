def getInt(message):
    try:
        number = int(input(message))
        return number

    except ValueError:
        print("Error: Please enter a valid integer!")
        return None

def getFloat(message):
    try:
        number = float(input(message))
        return number

    except ValueError:
        print("Error: Please enter a valid number!")
        return None
