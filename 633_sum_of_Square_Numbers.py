def judgeSquareSum(c):
    for a in range(c + 1):
        sqr_a = a * a
        if sqr_a > c:
            return False
        if ((c-sqr_a) ** 0.5)*10 % 10 == 0:
            return True
    # return False

c = 2
print(judgeSquareSum(c) == True)

c = 3
print(judgeSquareSum(c) == False)