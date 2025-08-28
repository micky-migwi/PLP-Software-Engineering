def calculate_discount(price, discount_percent):
    """
    Function to calculate the final price after applying a discount.
    If discount is 20% or higher, apply it; otherwise return original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    print(f"Final Price: {final_price:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values.")
