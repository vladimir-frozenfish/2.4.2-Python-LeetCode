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



s1 = 'abcdf'
s2 = 'abf'

print(prefix2strings(s1, s2))
