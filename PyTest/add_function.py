def addition(num1, num2):
    """This function gets two number as string converts them in integers
    and returns the output by adding them"""
    try:
        result = int(num1) + int(num2)
        return result

    except ValueError:
        print("Please enter a number.")


if __name__ == "__main__":
    print(addition(2, 3))
