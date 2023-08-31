

def main():
    print('Monthly Payment Loan Calculator\n')

    principal = float(input('Input the loan amount: '))
    apr = float(input("Input your apr: "))
    years = int(input('Input Years: '))

    monthly_interest_rate = apr / 1200
    months = years * 12
    monthly_payment = principal * monthly_interest_rate/(1 - (1 + monthly_interest_rate)**(-months)) 

    print("The monthly payment for this month is: %.2f ", monthly_payment)

main()