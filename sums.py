def sum_nums(lists, n):
    return sum(num for row in lists for num in row if num < n)

