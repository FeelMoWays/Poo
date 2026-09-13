def calculator():
    choice = input("Do you want to add,subtract,multiply or divide: ").lower()
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if choice == 'add':
        def add():
            return num1 +  num2
        return add()
    elif choice == 'subtract':
        def minus():
            return num1 - num2
        return minus()
    elif choice == 'multiply':
        def multiply():
            return num1 * num2
        return multiply()
    elif choice == 'divide':
        def divide():
            return num1 / num2
        return divide()
    else:
        return "Invalid Input"
print(calculator())

