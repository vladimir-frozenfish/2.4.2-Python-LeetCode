"""поиск самой длинной подстроки в строке"""


def lengthOfLongestSubstring(s: str) -> int:
    count = 0
    temp_count = 0
    temp_set = set()
    for i in range(len(s)):
        for j in s[i:]:

            if j not in temp_set:
                temp_set.add(j)
                temp_count += 1
            else:
                temp_set.clear()
                if temp_count > count:
                    count = temp_count

                temp_count = 0
                break

    if temp_count > count:
        count = temp_count

    return count

print(lengthOfLongestSubstring('pwwkew\"'))

