def calculate_tax(annual_salary):
    if annual_salary <= 15000:
        return annual_salary * 0.10
    elif annual_salary <= 75000:
        return annual_salary * 0.20
    elif annual_salary <= 200000:
        return annual_salary * 0.25
    else:
        return annual_salary * 0.30

def wheres_the_money(annual_salary, monthly_rent, monthly_bills, weekly_food, annual_travel):
    # Calculate annual expenses
    annual_rent = monthly_rent * 12
    annual_bills = monthly_bills * 12
    annual_food = weekly_food * 52
    annual_tax = calculate_tax(annual_salary)
    
    # Cap tax at $75,000
    if annual_tax > 75000:
        annual_tax = 75000
    
    # Calculate total expenses and extra
    total_expenses = annual_rent + annual_bills + annual_food + annual_travel + annual_tax
    extra = annual_salary - total_expenses
    
    # Prepare the output
    categories = [
        ("mortgage/rent", annual_rent),
        ("bills", annual_bills),
        ("food", annual_food),
        ("travel", annual_travel),
        ("tax", annual_tax),
        ("extra", extra),
    ]
    
    # Header
    print(f"{'-' * 90}")
    print(f"See the financial breakdown below, based on a salary of ${annual_salary:,.2f}")
    print(f"{'-' * 90}")

    for name, amount in categories:
        percentage = (amount / annual_salary) * 100
        bar_length = int(percentage)
        print(f"| {name:<13} | {amount:>12,.2f} | {percentage:6.1f}% | {'#' * bar_length}")

    print(f"{'-' * 90}")
    
    # Check for tax limit
    if annual_tax == 75000:
        print(">>> TAX LIMIT REACHED <<<")

    # Check for deficit
    if extra < 0:
        print(">>> WARNING: DEFICIT <<<")

# Example usage
wheres_the_money(40000, 2000, 300, 150, 4000)
