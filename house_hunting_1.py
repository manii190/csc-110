

def calculate_months(annual_salary,portion_saved,total_cost):
# This function calculates the number 
# of months required for making the down payment
    '''

This function estimates how many months are required
to accumulate money for a down, payment on a house
based on the annual salary,
the ratio of the amount set aside each month to the salary received.
and the total cost of the house we are building.
Args:
annual_salary(float): The amount of money the individual is paid within a year.
portion_saved(float): The portion of paycheck preserved monthly.
total_cost(float): Simply the total cost of the house.
    
Returns(int): It gives the number of months
required to have saved enough money in order to
buy the house through paying the down payment.
    '''

    rate = 0.04 # rate
    current_savings=0.0 # current saving at start
    portion_down_payment=0.25 # down_payment
    monthly_salary = annual_salary / 12# calculateing annual salary
    down_payment = total_cost * portion_down_payment
    months = 0 #count number of months
    while current_savings < down_payment:
        current_savings += current_savings * (rate / 12)
        current_savings += monthly_salary * portion_saved
        months += 1# number of months
    return months # return the total months required

