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