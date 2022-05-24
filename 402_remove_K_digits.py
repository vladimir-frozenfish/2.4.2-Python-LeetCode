def removeKdigits(num: str, k: int) -> str:
    return None



num = "1432219"
k = 3
print(removeKdigits(num, k) == "1219")

num = "10200"
k = 1
print(removeKdigits(num, k) == "200")

num = "10"
k = 2
print(removeKdigits(num, k) == "0")
