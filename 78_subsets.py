from itertools import combinations

def subsets(nums: list[int]) -> list[list[int]]:
    combinations_list = []
    for i in range(len(nums)+1):
        combinations_list += list(map(list, combinations(nums, i)))
    return combinations_list

nums = [1,2,3,4]
print(subsets(nums))