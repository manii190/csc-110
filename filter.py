def remove_zero_sides(numbers):
    for row in numbers:
        while len(row) > 0 and row[0] == 0:
            row.pop(0)  
        while len(row) > 0 and row[-1] == 0:
            row.pop(-1) 
    return numbers #return numbers
