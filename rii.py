def calculate_tax(annual_salary):
    """
    This function calculates the tax based on the annual salary.
    Args:
       annual_salary: Annual salary of the person
    Returns:
        It returns the tax on the annual salary.
    """
    if 15000 >= annual_salary >= 0:
        return annual_salary / 10
    elif 75000 >= annual_salary > 15000:
        return annual_salary / 5
    elif 200000 >= annual_salary > 75000:
        return annual_salary / 4
    elif annual_salary > 200000:
        return annual_salary * (3 / 10)
    else:
        return "Invalid entry"

def max_tax(annual_salary):
    """
    This function checks if the calculated tax exceeds $75,000.
    Args:
       annual_salary: Annual salary of the person
    Returns:
        The maximum tax to be paid, capped at $75,000.
    """
    if calculate_tax(annual_salary) >= 75000:
        return 75000
    else:
        return calculate_tax(annual_salary)

def wheres_the_money(annual_salary, rent, bills, food, travel):
    """
    This function calculates the financial breakdown based on salary and expenses.
    Args:
       annual_salary: Annual salary of the person
       rent: Monthly rent
       bills: Monthly bills
       food: Weekly food expenses
       travel: Annual travel expenses
    Returns:
        None (prints the financial breakdown).
    """

    # Calculate annual expenditures
    final_rent = float(rent * 12)
    final_bills = float(bills * 12)
    final_food = float(food * 52)
    final_travel = float(travel)
    tax = max_tax(annual_salary)

    # Calculate remaining salary after expenses
    extra = float(annual_salary - (final_rent + final_bills + final_food + final_travel + tax))

    # Format the values for better readability
    final_rent1 = '{:,.2f}'.format(final_rent)
    final_bills1 = '{:,.2f}'.format(final_bills)
    final_food1 = '{:,.2f}'.format(final_food)
    final_travel1 = '{:,.2f}'.format(final_travel)
    final_extra1 = '{:,.2f}'.format(extra)
    final_tax1 = '{:,.2f}'.format(tax)

    # Calculate percentages
    rent_percentage = round((final_rent * 100) / annual_salary, 1)
    bills_percentage = round((final_bills * 100) / annual_salary, 1)
    food_percentage = round((final_food * 100) / annual_salary, 1)
    travel_percentage = round((final_travel * 100) / annual_salary, 1)
    tax_percentage = round((tax * 100) / annual_salary, 1)
    extra_percentage = round((extra * 100) / annual_salary, 1)

    # Determine the maximum length for formatting
    length = max(len(final_rent1), len(final_bills1), len(final_food1), 
                len(final_travel1), len(final_tax1), len(final_extra1))

    # Print the financial breakdown table
    print('---------------------' + '-' * length)
    print(f'See the financial breakdown below, based on a salary of ${annual_salary:,.2f}')
    print('---------------------' + '-' * length)
    print(f'| mortgage/rent | $ {final_rent1} | {rent_percentage}% | {"#" * int(rent_percentage)}')
    print(f'|         bills | $ {final_bills1} | {bills_percentage}% | {"#" * int(bills_percentage)}')
    print(f'|          food | $ {final_food1} | {food_percentage}% | {"#" * int(food_percentage)}')
    print(f'|        travel | $ {final_travel1} | {travel_percentage}% | {"#" * int(travel_percentage)}')
    print(f'|           tax | $ {final_tax1} | {tax_percentage}% | {"#" * int(tax_percentage)}')
    print(f'|         extra | $ {final_extra1} | {extra_percentage}% | {"#" * int(extra_percentage)}')
    print('------------------' + '-' * length)

    # Warnings for deficits and tax limits
    if extra < 0:
        print('>>>> WARNING: DEFICIT <<<<')

    if tax >= 75000:
        print('>>> TAX LIMIT REACHED <<<')

def main():
    # Example usage
    wheres_the_money(30000, 700, 300, 200, 4000)

if __name__ == "__main__":
    main()
