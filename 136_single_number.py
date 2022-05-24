from collections import defaultdict

def singleNumber(nums):
    nums_dict = defaultdict(int)
    for i in nums:
        if nums_dict[i] == 1:
            nums_dict.pop(i)
        else:
            nums_dict[i] += 1

    return list(nums_dict.keys())[0]

nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))
