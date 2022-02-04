'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''


def prefix2strings(s1, s2):
    prefix = ''
    i = 0
    while i < len(s1) and i < len(s2):
        if s1[i] == s2[i]:
            prefix += s1[i]
            i += 1
        else:
            break
    return prefix


def longestCommonPrefix(strs: list[str]) -> str:
    prefix = strs[0]
    for i in range(1, len(strs)):
        prefix = prefix2strings(prefix, strs[i])
        if prefix == '':
            return ''
    return prefix

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs) == 'fl')

strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs) == '')


