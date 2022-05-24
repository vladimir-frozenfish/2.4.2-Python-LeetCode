"""Given a string columnTitle that represents the column title as appear in an Excel sheet,
return its corresponding column number."""

def titleToNumber(columnTitle):
    AZ_dict = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26,
    }

    number = 0
    len_value = len(columnTitle)
    for i in range(len_value):
        number += AZ_dict[columnTitle[i]] * (26 ** (len_value-i-1))
    return number


columnTitle = "A"
print(titleToNumber(columnTitle) == 1)

columnTitle = "B"
print(titleToNumber(columnTitle) == 2)

columnTitle = "AA"
print(titleToNumber(columnTitle) == 27)

columnTitle = "AB"
print(titleToNumber(columnTitle) == 28)

columnTitle = "ZY"
print(titleToNumber(columnTitle) == 701)


