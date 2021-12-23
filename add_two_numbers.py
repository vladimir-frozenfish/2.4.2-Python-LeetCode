"""Односвязные списки"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1_list = []
        while l1.next:
            l1_list.append(l1.val)
            l1 = l1.next
        l1_list.append(l1.val)

        l2_list = []
        while l2.next:
            l2_list.append(l2.val)
            l2 = l2.next
        l2_list.append(l2.val)

        l1_list = int(''.join(map(str, l1_list[::-1])))
        l2_list = int(''.join(map(str, l2_list[::-1])))

        lsum_list = list(str(l1_list + l2_list))

        lsum = ListNode(int(lsum_list[0]))
        for i in lsum_list[1:]:
            lsum = ListNode(int(i), next=lsum)

        # print(lsum)

        return lsum
