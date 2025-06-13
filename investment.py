def investment_years(initial_amount, goal_of_investment):
    result = initial_amount
    count = 0
    while result <= goal_of_investment*initial_amount :
        result *= (1.05)
        count +=1
    message = "The investment of ${:,} will be {} times larger in {} years.".format(initial_amount,goal_of_investment,count)
    return message

def main():
    initial_amount = 10000
    goal_of_investment = 2
    years_needed = investment_years(initial_amount, goal_of_investment)
    message_for_10000 = f"The investment of ${initial_amount:,} will be {goal_of_investment} times larger in {years_needed} years."
    print(message_for_10000)
    years_needed_50000 = investment_years(50000, 10)
    message_for_50000 = f"The investment of ${50000:,} will be {10} times larger in {years_needed_50000} years."
    print(message_for_50000)
    years_needed_3600 = investment_years(3600, 8)
    message_for_3600 = f"The investment of ${3600:,} will be {8} times larger in {years_needed_3600} years."
    print(message_for_3600)
    years_needed_500 = investment_years(500, 5)
    message_for_500 = f"The investment of ${500:,} will be {5} times larger in {years_needed_500} years."
    print(message_for_500)
main()