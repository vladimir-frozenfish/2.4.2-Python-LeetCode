def searchInsert(nums, target):
    if target <= nums[0]:
        return 0
    nums.append(target+1)
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        elif target < nums[i+1]:
            return i + 1



nums = [1,3,5,6]
target = 0
print(searchInsert(nums, target) == 0)

nums = [1,3,5,6]
target = 5
print(searchInsert(nums, target) == 2)

nums = [1,3,5,6]
target = 2
print(searchInsert(nums, target) == 1)

nums = [1,3,5,6]
target = 7
print(searchInsert(nums, target) == 4)