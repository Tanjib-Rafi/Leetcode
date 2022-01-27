# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        while(head!=None and head.val == val): #checking if head is none and head value is the target value
            head = head.next #so move the point to the next of head
            

        curr = head #temp header for accesing the head

        
        while(curr!=None and curr.next!=None): #checking if curr is none and current next value is also none

            if curr.next.val == val : #if curr next is target value so move to the next
                curr.next=curr.next.next          

            else:
                curr = curr.next #else iterate through the loop
                
        return head #returning the head
