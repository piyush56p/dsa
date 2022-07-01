# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if (head):
            if(head.next is None):
                return None
            else:
                curr = head
                k=0
                while(curr):
                    k=k+1
                    curr=curr.next
                if(k!=n):
                    prev = head
                    ptr = head.next
                    for i in range(0,k-n-1):
                        ptr = ptr.next
                        prev = prev.next

                    prev.next = prev.next.next
                    ptr.next = None
                elif(k==n):
                    ptr = head.next
                    head = ptr
                   
                return head
        
        else:
            return head
            
