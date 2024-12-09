# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_final=ListNode(0)
        result=result_final
        while l1 or l2:
            if not l1:
                sum_up=l2.val+result.val
                l2=l2.next
            elif not l2:
                sum_up=l1.val+result.val
                l1=l1.next
            else:
                sum_up=l1.val+l2.val+result.val
                l1=l1.next
                l2=l2.next
            result.val=(sum_up%10)
            result.next=ListNode(sum_up//10)
            result_front=result
            result=result.next
        if result:
            if not result.val:
                result_front.next=None
        return result_final