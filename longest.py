def longest_string(list):
    longest = None
    for dictionary in list:
        for value in dictionary.values():
            if type(value) == str:
                if longest is None or len(value) > len(longest):
                    longest = value
    return longest
