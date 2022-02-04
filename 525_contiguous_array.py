"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
"""

# не решена

def findMaxLength(nums: list[int]) -> int:
    temp1 = 0
    temp2 = 1
    z = 0
    nums.append(5)

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            temp2 += 1
        else:
            temp_z = (temp1 if temp1 < temp2 else temp2) * 2
            z = z if z > temp_z else temp_z

            temp1 = temp2
            temp2 = 1
    return z

nums = [0,0,1,1,1,0,0,0,0]
print(findMaxLength(nums) == 6)

nums = [0,1,0]
print(findMaxLength(nums) == 2)
