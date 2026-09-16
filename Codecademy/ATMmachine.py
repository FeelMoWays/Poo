Name = input("Enter your name")
Balance = int(input("Enter your balance"))
Pin = int(input("Enter a four digit Pin"))
def check(Pin):
    lives = 3
    temp_pin  = input("Please enter your four digit pin: ")
    while lives > 0:
        if temp_pin == Pin:
            lives -= 3
        else:
            print("{}")