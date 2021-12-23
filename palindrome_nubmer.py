def isPalindrome(x: int) -> bool:
    """
    функция определяет является ли число полиндромом
    """
    x = str(x)
    middle = len(x)//2
    return x[0:middle] == x[-1:-middle-1:-1]

print(isPalindrome(101) == True)
print(isPalindrome(-202) == False)
print(isPalindrome(123321) == True)
print(isPalindrome(1234567) == False)