def is_palindrome(str):
    n = len(str)
    for i in range(n):
        if str[i] != str[(n-1)-i]:
            return False
    
    return True

print(is_palindrome('radar'))
print(is_palindrome('cutes'))