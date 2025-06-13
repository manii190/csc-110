
def sum_all(numbers):
    index = 0
    sum = 0
    while index < len(numbers):
        n =numbers[index]
        sum += n
        index += 1
    return sum
def main():
    print(sum_all([2,2,2]))
    print(sum_all([1,2,1,1]))
    print(sum_all([]))
main()