'''
mani abhi ram reddy
CSC 110
Project 7
This code has multiple functions to implement a Benford's Law analysis.
'''
def csv_to_list(file_name):
    '''
    This function returns a list of numbers 
    in each line in the given file .
    Args:
        file_name : the file we need to check.
    Returns:
        numbers : list of numbers .
    '''
    a = open(file_name, 'r')
    numbers = []
    for line in a:
        chars = line.strip().split(",")
        for num in chars:
    # checks if numeric and adds to the list
            if num[0] in "123456789" :
                numbers.append(num)
    a.close()
    return numbers

def count_start_digits(numbers):
    '''
    This function returns the counts the first digit
    Args:
       numbers it is a list of numbers in the file
    Returns:
        count the first digit in the distanary
    '''
    counts = {}
    for num in numbers:
        leading_digit = int(num[0])
        if leading_digit  not in counts:
            counts[leading_digit ] = 0
        counts[leading_digit ] += 1
    return counts


def digit_percentages(counts):
    '''
    This function returns the percentage
    Args:
        count is the number of first digits 
    Returns:
    gives the percentage of first digit
    '''
    percent = {}
    sum = 0
    for index in counts:
        sum += counts[index]
    for index in range(1,10):
        percent[index] = round(counts[index]/sum*100,2)
    return percent
    
def print_plot(percent):
    '''
    This function returns the chart
    Args:
        gives the percentage of first digit
    Returns:
        .creates a chart
    '''
    
    for i in percent:
        print("{} | {}".format(i,'#'*int(percent[i])))




def check_benfords_law(percent):
    '''
    This function returns the true an false
    Args:
        gives the percentage of first digit
    Returns:
        it is the results that  weather it follows the law or not
    '''
    expected = {1: 30, 2: 17, 3: 12, 4: 9, 5: 7, 6: 6, 7: 5, 8: 5, 9: 4}
    for index in percent:
        observed = percent[index]
        expected_value = expected[index]
        if not (expected_value - 5 <= observed <= expected_value + 10):
            return False
    return True

