metrocard = input("Pls enter your name: ")
balance = int(input('Enter the intial balance: '))
ticket_price  = 10
def display(balance):
    choice = input("Press add to add balance: " "\n"
                "Press view to view balance: " "\n"
                "Press book to book a ticket: ").lower()
    if choice == 'add':
        add = int(input("Enter the amount you want to add: "))
        balance += add
        print(f"Your current balance is {balance}")
    elif choice == 'view':
        print(f"Your balance is {balance}")
    elif choice == 'book':
        if balance < ticket_price:
            print("Insufficent budget add more funds")
        else:
            balance -= ticket_price
            print("Your ticket has been booked successfully")
            print(f"Your remaining balance is {balance}")
    return balance

user_active = True
while user_active:
    option = input("Do you want to continue: ").lower()
    if option == 'yes':
        display(balance)
    else:
        print("Thank you for using our services")
        user_active = False