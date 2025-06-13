def count_vowels(string):
    counts = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0,"A": 0, "E": 0, "I": 0, "O": 0, "U": 0}
    for index in range(len(string)):
        char = string[index]
        if char in counts:
            counts[char] += 1
    return counts
