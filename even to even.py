def make_all_even(integers):
    integers=input("enter the integers")
    index = 0
    while index<len(integers):
        if integers[index]% 2== 1:
            integers[index]+= 1
        index += 1
    return integers

