# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        curr  = l3
        carry = 0
        while(l1 or l2):
            sum = 0
            if(l1 is None):
                sum = l2.val + carry
                l2 = l2.next
                if sum>9:
                    carry = int(sum/10)
                    sum = sum%10
                else:
                    carry=0
            elif(l2 is None):
                sum  = l1.val + carry
                l1 = l1.next
                if sum>9:
                    carry = int(sum/10)
                    sum = sum%10
                else:
                    carry = 0
            else:
                sum = l1.val+l2.val+carry
                l1 = l1.next
                l2=l2.next
                if(sum>9):
                    carry = int(sum/10)
                    sum  = sum%10
                else:
                    carry = 0
            l3.next = ListNode(sum)
            l3=l3.next
        if carry>0:
            l3.next = ListNode(carry)
        return curr.next
                    
                
                    
                    
