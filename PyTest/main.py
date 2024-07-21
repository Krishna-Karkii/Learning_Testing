from add_function import addition

print("Addition")
print("Press q to quit the program")
while True:
    first = input("Enter first number: ")
    if first.lower() == "q":
        break
    second = input("Enter second number: ")
    if second.lower() == "q":
        break
    result = addition(first, second)
    print(result)
