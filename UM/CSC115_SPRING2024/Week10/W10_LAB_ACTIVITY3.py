SALES_TAX = 0.05
COUNTY_TAX = 0.025

def showSale(purchase, stateTax, countyTax):
    print(f"Purchase amount: {purchase}")
    print(f"State tax: {stateTax}")
    print(f"County tax: {countyTax}")
    print(f" Total tax: {stateTax + countyTax}")
    print(f"Total sale: {purchase + stateTax + countyTax}")


def main():
    purchase_amount = float(input("Enter the purchase amount: "))
    state_tax = purchase_amount * SALES_TAX
    county_tax = purchase_amount * COUNTY_TAX
    showSale(purchase_amount, state_tax, county_tax)

main()