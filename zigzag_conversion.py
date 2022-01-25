def convert(s: str, numRows: int) -> str:
    len_string = len(s)
    string_zigzag = []
    sdvig = 2 * numRows - 2
    sdvig2 = sdvig-1

    if numRows == 1:
        return s

    i = 0
    while i < len_string:
        string_zigzag.append(s[i])
        i += sdvig

    for j in range(1, numRows-1):
        if j >= len_string:
            continue

        string_zigzag.append(s[j])

        k = sdvig2
        i = j + sdvig

        while k < len_string:
            string_zigzag.append(s[k])
            if i < len_string:
                string_zigzag.append(s[i])
            k += sdvig
            i += sdvig

        sdvig2 -= 1

    i = numRows - 1
    while i < len_string:
        string_zigzag.append(s[i])
        i += sdvig

    # print(''.join(string_zigzag))
    return ''.join(string_zigzag)

s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows) == "PAHNAPLSIIGYIR")

s = "PAYPALISHIRING"
numRows = 4
print(convert(s, numRows) == "PINALSIGYAHRPI")

s = "A"
numRows = 3
print(convert(s, numRows) == "A")