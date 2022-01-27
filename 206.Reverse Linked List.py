# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
        prev = None #taking a prev variable with none 
        
        while head!=None:
          
            nextValue = head.next #storing next value because after reverse the head with prev link will be broke
            head.next = prev
            prev = head
            head = nextValue #now store head as nextValue which is separed
            
        return prev #returning the prev because at last prev will be at last value and head will be at null
            
     
