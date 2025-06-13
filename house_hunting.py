def calculate_months(annual_salary,portion_saved,total_cost):
    rate = 0.04
    current_savings=0.0
    portion_down_payment=0.25
    monthly_salary = annual_salary / 12
    down_payment = total_cost * portion_down_payment
    months = 0
    while current_savings < down_payment:
        current_savings += current_savings * (rate / 12)
        current_savings += monthly_salary * portion_saved
        months += 1
    return months