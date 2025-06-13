def calculate_tax(annual_salary):
    if annual_salary <= 15000:
        tax_percentage = 10
    elif annual_salary <= 75000:
        tax_percentage = 20
    elif annual_salary <= 200000:
        tax_percentage = 25
    else:
        tax_percentage = 30
    return annual_salary * (tax_percentage / 100.0)

def excess(annual_mortgage, annual_bills, annual_food, annual_travel, tax, annual_salary):
    total_expenses = annual_mortgage + annual_bills + annual_food + annual_travel + tax
    return annual_salary - total_expenses

def wheres_the_money(annual_salary, monthly_mortgage, monthly_bills, weekly_food, annual_travel):
    # Calculate annual expenses
    annual_mortgage = monthly_mortgage * 12
    annual_bills = monthly_bills * 12
    annual_food = weekly_food * 52
    tax = calculate_tax(annual_salary)

    # Cap tax at $75,000
    if tax > 75000:
        tax = 75000

    # Calculate excess money
    excess_amount = excess(annual_mortgage, annual_bills, annual_food, annual_travel, tax, annual_salary)

    # Format outputs
    planned_annual_mortgage = '{:,.2f}'.format(annual_mortgage)
    planned_annual_bills = '{:,.2f}'.format(annual_bills)
    planned_annual_food = '{:,.2f}'.format(annual_food)
    planned_annual_travel = '{:,.2f}'.format(annual_travel)
    planned_tax = '{:,.2f}'.format(tax)
    planned_excess = '{:,.2f}'.format(excess_amount)

    rent_percentage = round((annual_mortgage * 100) / annual_salary, 1)
    bills_percentage = round((annual_bills * 100) / annual_salary, 1)
    food_percentage = round((annual_food * 100) / annual_salary, 1)
    travel_percentage = round((annual_travel * 100) / annual_salary, 1)
    tax_percentage = round((tax * 100) / annual_salary, 1)
    extra_percentage = round((excess_amount * 100) / annual_salary, 1)

    length = max(len(planned_annual_mortgage), len(planned_annual_bills),
                 len(planned_annual_food), len(planned_annual_travel),
                 len(planned_tax), len(planned_excess))
    
    # Output
    print('---------------------' + '-' * length)
    print(f'See the financial breakdown below, based on a salary of ${annual_salary:,.2f}')
    print('---------------------' + '-' * length)
    
    print(f'| Planned Annual Mortgage | ${planned_annual_mortgage} | {rent_percentage}% | {"#" * int(rent_percentage)}')
    print(f'| Planned Annual Bills    | ${planned_annual_bills} | {bills_percentage}% | {"#" * int(bills_percentage)}')
    print(f'| Planned Annual Food     | ${planned_annual_food} | {food_percentage}% | {"#" * int(food_percentage)}')
    print(f'| Planned Annual Travel   | ${planned_annual_travel} | {travel_percentage}% | {"#" * int(travel_percentage)}')
    print(f'| Planned Tax            | ${planned_tax} | {tax_percentage}% | {"#" * int(tax_percentage)}')
    print(f'| Planned Excess         | ${planned_excess} | {extra_percentage}% | {"#" * int(extra_percentage)}')
    print('---------------------' + '-' * length)
    
    if excess_amount < 0:
        print('>>> WARNING: DEFICIT <<<')
    if tax >= 75000:
        print('>>> TAX LIMIT REACHED <<<')

def main():
    wheres_the_money(40000, 2000, 300, 150, 4000)

if __name__ == "__main__":
    main()
