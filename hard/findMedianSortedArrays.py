def findMedianSortedArrays(nums1, nums2):
    """поиск медианы двух отсротированных списков"""

    """сначала необходимо объединить два списка, менее затрантныс способом"""
    len1 = len(nums1)
    len2 = len(nums2)

    i_1 = 0
    i_2 = 0

    while i_1 < 0 and i_2 < 0:
        pass

    return None



nums1 = [1, 3, 5, 10]
nums2 = [2, 3, 6, 7, 9, 12]

merge_nums = sorted(nums1 + nums2)


mediana = findMedianSortedArrays(nums1, nums2)