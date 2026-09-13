def mortgage():
    intial_loan_amount = int(input("Enter your loan amount: "))
    down_payment = int(input("Enter your down payment: "))
    loan_amount = intial_loan_amount - down_payment
    intrest_rate = float(input("Enter your intrest rate: "))
    loan_term  = int(input("Enter you loan term in years: "))
    monthly_intrest = intrest_rate / 1200
    loan_term_in_months = loan_term * 12
    monthly_payment = (loan_amount * 
                       (monthly_intrest * 
                        (1 + monthly_intrest) ** loan_term_in_months))/(
                            (1 + monthly_intrest) ** loan_term_in_months - 1)
    print(f"Your monthly payment for the loan amount {intial_loan_amount} with down payment of {down_payment} for {loan_term} at {intrest_rate} is {monthly_payment} ") 

choice = input("Do you want to use our services: ").lower()
if choice == 'yes':
    mortgage()
    print("Thank you for using our service")
elif choice == 'no':
    print("Thank your for coming by")
else:
    print("Invalid choice")