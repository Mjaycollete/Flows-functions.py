def calculate_discount(price, discount_percent):
    """
    Returns the final price after applying a discount
    only if discount_percent is 20% or higher.
    Otherwise, returns the original price.
    """
    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
        return final_price
    else:
        return price


# --- Program starts here ---
# Prompt the user for inputs
price_input = float(input("Enter the original price: "))
discount_input = float(input("Enter the discount percentage: "))

# Calculate the final price using the function
final_price = calculate_discount(price_input, discount_input)

# Print the result (formatted to 2 decimal places)
print(f"Final price: {final_price:.2f}")
