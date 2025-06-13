def count_vowels(string):
    count =0
    index =0
    while index <len(string):
        count +=(string[index] in "aeiouAEIOU" )
        index += 1
    return count
def main():
    print(count_vowels(""))
    print(count_vowels("aaa"))
    print(count_vowels("AEIOU"))
    print(count_vowels("cysts"))
main()
