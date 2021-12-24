def findMedianSortedArrays(nums1, nums2):
    """поиск медианы двух отсротированных списков"""

    len1 = len(nums1)
    len2 = len(nums2)

    """объединение двух списков"""
    i_1 = 0
    i_2 = 0
    merge_nums = []
    while i_1 < len1 and i_2 < len2:
        if nums1[i_1] < nums2[i_2]:
            merge_nums.append(nums1[i_1])
            i_1 += 1
        else:
            merge_nums.append(nums2[i_2])
            i_2 += 1

    merge_nums += nums1[i_1:] + nums2[i_2:]

    """нахождение медианы объединенного списка"""
    middle = (len1 + len2) // 2
    """если длинна списка нечетная"""
    if (len1 + len2) % 2:
        return merge_nums[middle]
    """если длинна списка четная"""
    return (merge_nums[middle - 1] + merge_nums[middle]) / 2




nums1 = [1, 3, 5, 10, 22]
nums2 = [2, 3, 6, 7, 9, 12]

merge_nums = sorted(nums1 + nums2)
print(merge_nums)


mediana = findMedianSortedArrays(nums1, nums2)
print(mediana)