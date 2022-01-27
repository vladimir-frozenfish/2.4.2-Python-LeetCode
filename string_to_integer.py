def myAtoi(s: str) -> int:
    """функция возвращает число из строки"""
    '''
    if not s:
        return 0
    '''

    number = []
    for i in range(len(s)):
        if s[i].isdigit():
            number.append(s[i])
        elif (s[i] == '-' or s[i] == '+') and s[i+1:i+2].isdigit() and not number:
            number.append(s[i])
        elif not s[i].isdigit() and not number and not s[i] == ' ':
            return 0
        elif not s[i].isdigit() and number:
            break

    if number:
        number = int(''.join(number))
    else:
        return 0

    if number < -2147483648:
        return -2147483648
    elif number > 2147483647:
        return 2147483647

    return number

print(myAtoi('42') == 42)
print(myAtoi('    -42') == -42)
print(myAtoi('sdff s 45 sdf') == 0)

print(myAtoi('sdff s 45 sf  sdf34df') == 0)
print(myAtoi('9837498729384734') == 2147483647)
print(myAtoi('34.34') == 34)

print(myAtoi('') == 0)
print(myAtoi('sdfsdfsdf') == 0)
print(myAtoi('-') == 0)

print(myAtoi('+1') == 1)

print(myAtoi('000000-42') == 0)


