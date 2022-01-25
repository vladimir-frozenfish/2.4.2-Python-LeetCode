def reverse(x: int) -> int:
    """функция возращает реверс заданного числа,
    если возвращаемое число не 32 битное, возвращает 0"""
    number = int(str(abs(x))[::-1])

    if x < 0:
        number = -number

    if number < - 2 ** 31 or number > 2 ** 31 - 1:
        return 0

    return number


print(reverse(123456) == 654321)
print(reverse(-123456) == -654321)
print(reverse(34234234234324123456) == 0)
