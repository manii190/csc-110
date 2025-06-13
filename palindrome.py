def reverse_string(s):
    reversed_str = ""
    index = len(s) - 1
    while index >= 0:
        reversed_str += s[index]
        index -= 1
    return reversed_str
def remove_spaces(rs):
    no_space_str = ""
    index = 0
    while index < len(rs):
        no_space_str += rs[index] * (rs[index] != ' ')
        index += 1
    return no_space_str
def is_palindrome(p):
    cleaned_str = remove_spaces(p)
    reversed_str = reverse_string(cleaned_str)
    index = 0
    palindrome = True
    while index < len(cleaned_str):
        palindrome *= (cleaned_str[index] == reversed_str[index])
        index += 1
    return bool(palindrome)
def main():
    print(reverse_string("aeiou"))
    print(remove_spaces("ae io ua"))
    print(is_palindrome("noon"))
    print(is_palindrome("deified"))
    print(is_palindrome("go deliver a dare vile dog"))
main()
