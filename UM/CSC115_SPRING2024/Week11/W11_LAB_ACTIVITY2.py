def is_sale_valid(amount):
    if amount > 0.0:
        return True
    else:
        return False


# --------------------------------------


def get_sales():
    monthly_sales = int(input("Enter the monthly sales: "))
    while not is_sale_valid(monthly_sales):
        monthly_sales = float(
            input("Invalid Input Amount. Please Re-enter the monthly sales: ")
        )
    return monthly_sales


# --------------------------------------


def get_advanced_pay():
    advance_pay = float(input("Enter the amount of advanced pay, or enter 0 if no pay was given: "))
    while advance_pay > 2000 or advance_pay < 0:
        advance_pay = float(
            input("Invalid Input Amount. Please Re-enter the amount of advanced pay, or enter 0 if no advanced pay was given: "))
    return advance_pay


# --------------------------------------


def determine_commission_rate(sales_amount):
    if (sales_amount < 1000):
        return 0.1
    elif (sales_amount <= 14999.99):
        return 0.12
    elif (sales_amount <= 17999.99):
        return 0.14
    elif (sales_amount <= 21999.99):
        return 0.16
    else:
        return 0.18


# --------------------------------------


def show_commision_and_paycheck(sales_amount, commision_rate, commision_amount, advance_pay, pay_amount):
    print("-" * 20)
    print('-----Pay CHeck Calculation-----')
    print("-" * 20)
    print(f"Sales Amount: ${sales_amount:,.2f}")
    print(f"Commision Rate: {commision_rate * 100:,.2f}%")
    print(f"Commision Amount: ${commision_amount:,.2f}")
    print(f"Advanced Pay Amount: ${advance_pay:,.2f}")
    print(f"Paycheck Amount: ${pay_amount:,.2f}")
    
    if pay_amount < 0:
        print("You have must reimburse the company.")
    print('-' * 20)



# --------------------------------------


def main():
    # Get the amount of sales.
    sales = get_sales()
    # Get the amount of advanced pay.
    advanced_pay_amount = get_advanced_pay()
    # Determine the commission rate.
    commission_rate = determine_commission_rate(sales)
    # Determine the commission amount.
    commission_amount = sales * commission_rate
    # Calculate the paycheck.
    paycheck_amount = commission_amount - advanced_pay_amount
    # Show the commission and paycheck.
    show_commision_and_paycheck(
        sales, commission_rate, commission_amount, advanced_pay_amount, paycheck_amount
    )


if __name__ == "__main__":
    main()
