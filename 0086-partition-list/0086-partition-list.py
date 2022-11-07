# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_a, dummy_b = ListNode(), ListNode()
        pa, pb = dummy_a, dummy_b
        while head is not None:
            if head.val < x:
                pa.next = head; pa = pa.next
            else:
                pb.next = head; pb = pb.next
            head = head.next
        # warn
        pb.next = None
        pa.next = dummy_b.next
        return dummy_a.next
        
