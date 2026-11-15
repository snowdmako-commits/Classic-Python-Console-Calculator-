def getInt(message):
    try:
        number = int(input(message))
        return number

    except ValueError:
        print("Error: Please enter a valid integer!")
        return None