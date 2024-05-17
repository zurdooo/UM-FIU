PROPERTY_TAX_PERCENT = 0.0072
ASSESS_PERCENT = 0.6


def show_property_tax(assetValue, propertyTax):
    print(f"The property tax on ${assetValue:.2f} is ${(propertyTax):.2f}")

def main():
    assetValue = float(input("Enter the actual value of the asset: "))
    assessed_value = assetValue * ASSESS_PERCENT
    property_tax = assessed_value * PROPERTY_TAX_PERCENT
    show_property_tax(assessed_value, property_tax)


main()
