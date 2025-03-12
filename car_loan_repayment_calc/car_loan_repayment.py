import logging

def calculate_monthly_repayment(car_price: float, number_of_years: int, annual_interest_rate: float, deposit: float) -> tuple[float, int, float, float]:
    if car_price < 0:
        raise ValueError("Car price cannot be negative")
    
    if number_of_years < 0:
        raise ValueError("Number of years cannot be negative")
    
    if annual_interest_rate < 0:
        raise ValueError("Annual interest rate cannot be negative")
    
    if deposit < 0 or deposit > car_price:
        raise ValueError("Deposit cannot be negative or greater than car price")
    

    loan_amount = car_price - deposit

    monthly_interest_rate = annual_interest_rate/(12*100)

    number_of_payments = number_of_years * 12

    if monthly_interest_rate == 0:
        monthly_repayment = loan_amount/number_of_payments
    else:
        monthly_repayment = loan_amount * monthly_interest_rate/(1-(1+monthly_interest_rate)**(-number_of_payments))

    return monthly_repayment, 

def get_user_input() -> tuple[float, int, float, float]:
    try:
        car_price = float(input("Enter car price:"))
        number_of_years = int(input("Enter number of years: "))
        annual_interest_rate = float(input("Enter annual interest rate: "))
        deposit = float(input("Enter deposit (put 0 if no deposit): "))

    except ValueError as e:
        logging.error("Invalid input. Please enter numeric values.")
        raise ValueError("Invalid input. Please enter a valid number")
    
    return car_price, number_of_years, annual_interest_rate, deposit

def main():
    car_price, number_of_years, annual_interest_rate, deposit = get_user_input()
    monthly_repayment = calculate_monthly_repayment(car_price, number_of_years, annual_interest_rate, deposit)
    print(f"Monthly repayment: {monthly_repayment}")

# entry point
if __name__ == "__main__":
    main()


