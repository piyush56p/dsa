# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            curr = head.next
            prev = head
            while(curr):
                if prev.val == curr.val:
                    if (curr.next):
                        prev.next = curr.next
                    else:
                        prev.next = None
                    curr = curr.next
                else:
                    prev = curr
                    curr = curr.next
                    
            return head
            
