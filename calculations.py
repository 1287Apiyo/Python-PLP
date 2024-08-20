def calculate_discount(price, discount_percent):
    # Calculate the discount amount and final price
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
    else:
        final_price = price
    return final_price

# Prompt the user to enter the original price and discount percentage
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percent)
    
    # Print the final price
    print("The final price after applying the discount is: {:.2f}".format(final_price))
except ValueError:
    print("Please enter valid numbers for price and discount percentage.")
