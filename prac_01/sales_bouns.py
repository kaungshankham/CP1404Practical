"""
    Program to calculate and display a user's bonus based on sales.
    If sales are under $1,000, the user gets a 10% bonus.
    If sales are $1,000 or over, the bonus is 15%.
"""

BONUS_ON_SALES = 1000
MINIMUM_DISCOUNT_RATE = 0.10
MAXIMUM_DISCOUNT_RATE = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < BONUS_ON_SALES:
        bonus = sales * MINIMUM_DISCOUNT_RATE
    else:
        bonus = sales * MAXIMUM_DISCOUNT_RATE
    print(f"The bonus is ${bonus}")
    sales = float(input("Enter sales: $"))
