"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

def isValid(s: str) -> bool:
    parentheses = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    queue_parentheses = []
    for i in s:
        if i in parentheses:
            if not queue_parentheses or queue_parentheses.pop() != parentheses[i]:
                return False
        else:
            queue_parentheses.append(i)

    if queue_parentheses:
        return False
    return True


print(isValid('(){}[]') == True)
print(isValid('){}[]') == False)
print(isValid('(){(}[]') == False)
print(isValid('((((((((((((((((({{{[][][]}}}))))))))))))))))){}') == True)
print(isValid('(((((((') == False)
