def is_palindrome(string):
    left_pos = 0
    right_pos = len(string) - 1

    while right_pos > left_pos:
        if not string[left_pos]== string[right_pos]:
            return False
        left_pos += 1
        right_pos -= 1
        return True
print(is_palindrome("madam"))
print(is_palindrome("hello"))
print(is_palindrome("racecar"))
print(is_palindrome("python"))